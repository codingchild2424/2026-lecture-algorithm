/* ======================================================================
   Hash Table Explorer -- Frontend Logic
   ====================================================================== */

document.addEventListener("DOMContentLoaded", () => {
    // -----------------------------------------------------------------
    // Tab switching
    // -----------------------------------------------------------------
    const tabBtns = document.querySelectorAll(".tab-btn");
    const panels  = document.querySelectorAll(".tab-panel");

    tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            tabBtns.forEach(b => b.classList.remove("active"));
            panels.forEach(p => p.classList.remove("active"));
            btn.classList.add("active");
            document.getElementById(btn.dataset.tab).classList.add("active");
        });
    });

    // -----------------------------------------------------------------
    // Helper: POST JSON to API
    // -----------------------------------------------------------------
    async function apiPost(url, body) {
        const res = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body),
        });
        return res.json();
    }

    // -----------------------------------------------------------------
    // Helper: parse numbers from input string
    // -----------------------------------------------------------------
    function parseNumbers(str) {
        return str
            .split(/[\s,]+/)
            .filter(s => s !== "")
            .map(Number)
            .filter(n => !isNaN(n));
    }

    // -----------------------------------------------------------------
    // Helper: render stats row
    // -----------------------------------------------------------------
    function renderStats(container, stats) {
        container.innerHTML = stats.map(s =>
            `<div class="stat-box">
                <div class="stat-value">${s.value}</div>
                <div class="stat-label">${s.label}</div>
            </div>`
        ).join("");
    }

    // =================================================================
    // 1. HASH TABLE VISUALIZATION
    // =================================================================
    const vizMethod  = document.getElementById("viz-method");
    const vizSize    = document.getElementById("viz-size");
    const vizKey     = document.getElementById("viz-key");
    const vizValue   = document.getElementById("viz-value");
    const vizInitBtn = document.getElementById("viz-init");
    const vizInsert  = document.getElementById("viz-insert");
    const vizSearch  = document.getElementById("viz-search");
    const vizDelete  = document.getElementById("viz-delete");
    const vizRandom  = document.getElementById("viz-random");
    const vizStats   = document.getElementById("viz-stats");
    const vizTable   = document.getElementById("viz-table");
    const vizLog     = document.getElementById("viz-log");
    const vizHashDetail = document.getElementById("viz-hash-detail");
    const vizHashSteps  = document.getElementById("viz-hash-steps");

    let vizLogEntries = [];

    // Render chaining hash table
    function renderChainingTable(snapshot, highlightKey) {
        let html = "";
        snapshot.buckets.forEach(bucket => {
            html += `<div class="bucket-row">`;
            html += `<div class="bucket-index">${bucket.index}</div>`;
            html += `<div class="bucket-content">`;
            if (bucket.entries.length === 0) {
                html += `<span class="bucket-empty">empty</span>`;
            } else {
                bucket.entries.forEach((entry, i) => {
                    if (i > 0) html += `<span class="chain-arrow">&#8594;</span>`;
                    const hl = (String(entry.key) === String(highlightKey)) ? " highlight" : "";
                    const val = entry.value ? ` : ${entry.value}` : "";
                    html += `<span class="chain-node${hl}">${entry.key}${val}</span>`;
                });
            }
            html += `</div></div>`;
        });
        vizTable.innerHTML = html;
    }

    // Render linear probing hash table
    function renderProbingTable(snapshot, highlightKey, probeSequence) {
        const probeSet = new Set(probeSequence || []);
        let html = `<div class="slot-grid">`;
        snapshot.slots.forEach(slot => {
            let cls = slot.state;
            if (String(slot.key) === String(highlightKey)) cls += " highlight";
            else if (probeSet.has(slot.index)) cls += " probe-highlight";
            html += `<div class="slot-cell ${cls}">`;
            html += `<div class="slot-idx">[${slot.index}]</div>`;
            if (slot.state === "occupied") {
                const val = slot.value ? `<div style="font-size:0.7rem;color:var(--text-muted)">${slot.value}</div>` : "";
                html += `<div class="slot-key">${slot.key}</div>${val}`;
            } else if (slot.state === "deleted") {
                html += `<div class="slot-key">DEL</div>`;
            } else {
                html += `<div style="color:var(--text-muted);font-size:0.75rem">--</div>`;
            }
            html += `</div>`;
        });
        html += `</div>`;
        vizTable.innerHTML = html;
    }

    // Render the table based on snapshot type
    function renderVizSnapshot(snapshot, highlightKey, probeSequence) {
        if (snapshot.type === "chaining") {
            renderStats(vizStats, [
                { label: "Size", value: snapshot.size },
                { label: "Count", value: snapshot.count },
                { label: "Load Factor", value: snapshot.load_factor },
                { label: "Collisions", value: snapshot.collisions },
                { label: "Avg Chain", value: snapshot.avg_chain_length },
            ]);
            renderChainingTable(snapshot, highlightKey);
        } else {
            renderStats(vizStats, [
                { label: "Size", value: snapshot.size },
                { label: "Count", value: snapshot.count },
                { label: "Load Factor", value: snapshot.load_factor },
                { label: "Collisions", value: snapshot.collisions },
                { label: "Avg Probes", value: snapshot.avg_probe_length },
            ]);
            renderProbingTable(snapshot, highlightKey, probeSequence);
        }
    }

    // Show hash computation details
    function showHashDetail(op) {
        if (!op || !op.hash_computation) {
            vizHashDetail.style.display = "none";
            return;
        }
        vizHashDetail.style.display = "";
        let text = `Key: ${op.key}\n`;
        text += `Hash: ${op.hash_computation}\n`;
        text += `Bucket index: ${op.hash_value}\n`;
        if (op.probe_sequence) {
            text += `Probe sequence: [${op.probe_sequence.join(" -> ")}]\n`;
        }
        if (op.probes !== undefined) {
            text += `Probes needed: ${op.probes}\n`;
        }
        if (op.collision !== undefined) {
            text += `Collision: ${op.collision ? "YES" : "no"}\n`;
        }
        vizHashSteps.textContent = text;
    }

    // Add to operation log
    function addToVizLog(op) {
        if (!op) return;
        let entry = `[${op.operation}] key=${op.key}`;
        if (op.hash_value !== undefined) entry += `, hash=${op.hash_value}`;
        if (op.found !== undefined) entry += `, found=${op.found}`;
        if (op.action) entry += `, ${op.action}`;
        if (op.probes !== undefined) entry += `, probes=${op.probes}`;
        if (op.collision) entry += ` (COLLISION)`;
        vizLogEntries.push(entry);
        vizLog.textContent = vizLogEntries.join("\n");
        vizLog.scrollTop = vizLog.scrollHeight;
    }

    // Initialize
    vizInitBtn.addEventListener("click", async () => {
        vizLogEntries = [];
        vizLog.textContent = "";
        vizHashDetail.style.display = "none";
        const data = await apiPost("/api/hashtable/init", {
            size: parseInt(vizSize.value) || 11,
            method: vizMethod.value,
        });
        renderVizSnapshot(data, null, null);
    });

    // Perform operation
    async function vizOp(operation) {
        const key = vizKey.value.trim();
        if (!key) { alert("Please enter a key."); return; }
        const data = await apiPost("/api/hashtable/op", {
            method: vizMethod.value,
            operation: operation,
            key: key,
            value: vizValue.value.trim() || null,
        });
        if (data.error) { alert(data.error); return; }
        const op = data.last_operation;
        const probeSeq = op ? op.probe_sequence : null;
        renderVizSnapshot(data, key, probeSeq);
        showHashDetail(op);
        addToVizLog(op);
    }

    vizInsert.addEventListener("click", () => vizOp("insert"));
    vizSearch.addEventListener("click", () => vizOp("search"));
    vizDelete.addEventListener("click", () => vizOp("delete"));

    // Insert 5 random keys
    vizRandom.addEventListener("click", async () => {
        for (let i = 0; i < 5; i++) {
            const k = Math.floor(Math.random() * 100);
            vizKey.value = String(k);
            vizValue.value = "";
            await vizOp("insert");
        }
    });

    // Auto-init on page load
    vizInitBtn.click();


    // =================================================================
    // 2. COLLISION RESOLUTION COMPARISON
    // =================================================================
    const cmpN      = document.getElementById("cmp-n");
    const cmpSize   = document.getElementById("cmp-size");
    const cmpRange  = document.getElementById("cmp-range");
    const cmpRunBtn = document.getElementById("cmp-run");
    const cmpResult = document.getElementById("cmp-result");

    cmpRunBtn.addEventListener("click", async () => {
        cmpResult.innerHTML = '<div class="card"><span class="spinner"></span> Running comparison...</div>';
        const data = await apiPost("/api/hashtable/compare", {
            n: parseInt(cmpN.value) || 20,
            table_size: parseInt(cmpSize.value) || 11,
            key_range: parseInt(cmpRange.value) || 200,
        });

        let html = "";

        // Summary table
        html += `<div class="card">
            <h2>Summary</h2>
            <p class="info">Inserted ${data.n} keys into tables of size ${data.table_size}.
               Load factor = ${data.n} / ${data.table_size} = ${(data.n / data.table_size).toFixed(2)}</p>
            <table class="cmp-table">
                <tr>
                    <th>Metric</th>
                    <th>Chaining</th>
                    <th>Linear Probing</th>
                </tr>
                <tr>
                    <td><strong>Items Stored</strong></td>
                    <td>${data.chaining.snapshot.count}</td>
                    <td>${data.probing.items_inserted} ${data.probing.items_inserted < data.n ? '<span class="tag tag-amber">TABLE FULL</span>' : ''}</td>
                </tr>
                <tr>
                    <td><strong>Collisions</strong></td>
                    <td>${data.chaining.collisions}</td>
                    <td>${data.probing.collisions}</td>
                </tr>
                <tr>
                    <td><strong>Load Factor</strong></td>
                    <td>${data.chaining.load_factor}</td>
                    <td>${data.probing.load_factor}</td>
                </tr>
                <tr>
                    <td><strong>Avg Chain / Probe Length</strong></td>
                    <td>${data.chaining.avg_chain_length}</td>
                    <td>${data.probing.avg_probe_length}</td>
                </tr>
                <tr>
                    <td><strong>Avg Search Probes</strong></td>
                    <td>${data.search_comparison.chaining_avg}</td>
                    <td>${data.search_comparison.probing_avg}</td>
                </tr>
            </table>
        </div>`;

        // Bar charts for collisions and probes
        html += `<div class="card">
            <h2>Collision Comparison</h2>
            <div class="bar-chart">
                <div class="bar-row">
                    <span class="bar-label">Chaining</span>
                    <div class="bar-track"><div class="bar-fill c0" style="width:${pct(data.chaining.collisions, Math.max(data.chaining.collisions, data.probing.collisions))}%"></div></div>
                    <span class="bar-value">${data.chaining.collisions} collisions</span>
                </div>
                <div class="bar-row">
                    <span class="bar-label">Linear Probing</span>
                    <div class="bar-track"><div class="bar-fill c3" style="width:${pct(data.probing.collisions, Math.max(data.chaining.collisions, data.probing.collisions))}%"></div></div>
                    <span class="bar-value">${data.probing.collisions} collisions</span>
                </div>
            </div>
            <h3>Average Search Probes</h3>
            <div class="bar-chart">
                <div class="bar-row">
                    <span class="bar-label">Chaining</span>
                    <div class="bar-track"><div class="bar-fill c0" style="width:${pct(data.search_comparison.chaining_avg, Math.max(data.search_comparison.chaining_avg, data.search_comparison.probing_avg))}%"></div></div>
                    <span class="bar-value">${data.search_comparison.chaining_avg} probes</span>
                </div>
                <div class="bar-row">
                    <span class="bar-label">Linear Probing</span>
                    <div class="bar-track"><div class="bar-fill c3" style="width:${pct(data.search_comparison.probing_avg, Math.max(data.search_comparison.chaining_avg, data.search_comparison.probing_avg))}%"></div></div>
                    <span class="bar-value">${data.search_comparison.probing_avg} probes</span>
                </div>
            </div>
        </div>`;

        // Side-by-side table snapshots
        html += `<div class="two-col">`;

        // Chaining snapshot
        html += `<div class="card"><h2>Chaining Table</h2>`;
        data.chaining.snapshot.buckets.forEach(bucket => {
            html += `<div class="bucket-row">`;
            html += `<div class="bucket-index">${bucket.index}</div>`;
            html += `<div class="bucket-content">`;
            if (bucket.entries.length === 0) {
                html += `<span class="bucket-empty">empty</span>`;
            } else {
                bucket.entries.forEach((entry, i) => {
                    if (i > 0) html += `<span class="chain-arrow">&#8594;</span>`;
                    html += `<span class="chain-node">${entry.key}</span>`;
                });
            }
            html += `</div></div>`;
        });
        html += `</div>`;

        // Probing snapshot
        html += `<div class="card"><h2>Linear Probing Table</h2>`;
        html += `<div class="slot-grid">`;
        data.probing.snapshot.slots.forEach(slot => {
            html += `<div class="slot-cell ${slot.state}">`;
            html += `<div class="slot-idx">[${slot.index}]</div>`;
            if (slot.state === "occupied") {
                html += `<div class="slot-key">${slot.key}</div>`;
            } else {
                html += `<div style="color:var(--text-muted);font-size:0.75rem">--</div>`;
            }
            html += `</div>`;
        });
        html += `</div></div>`;

        html += `</div>`; // close two-col

        // Insert steps log (first few)
        html += `<div class="card">
            <h2>Insert Steps (First 15)</h2>
            <div class="two-col">
                <div>
                    <h3>Chaining</h3>
                    <div class="result-area" style="max-height:250px">`;
        data.chaining.insert_steps.slice(0, 15).forEach((s, i) => {
            html += `${i + 1}. Insert ${s.key} -> bucket[${s.hash_value}]`;
            if (s.collision) html += ` (COLLISION, chain=${s.chain_length_after})`;
            html += `\n`;
        });
        html += `</div></div>
                <div>
                    <h3>Linear Probing</h3>
                    <div class="result-area" style="max-height:250px">`;
        data.probing.insert_steps.slice(0, 15).forEach((s, i) => {
            html += `${i + 1}. Insert ${s.key} -> hash=${s.hash_value}`;
            if (s.collision) html += `, probed to [${s.final_index}] (${s.probes} probes)`;
            else html += `, placed at [${s.final_index}]`;
            html += `\n`;
        });
        html += `</div></div>
            </div>
        </div>`;

        // Keys inserted
        html += `<div class="card">
            <h2>Keys Inserted</h2>
            <p class="info">[${data.keys_inserted.join(", ")}]</p>
        </div>`;

        cmpResult.innerHTML = html;
    });

    function pct(val, max) {
        if (!max || max === 0) return 1;
        return Math.max((val / max) * 100, 1).toFixed(1);
    }


    // =================================================================
    // 3. PHONE BOOK
    // =================================================================
    const pbSize    = document.getElementById("pb-size");
    const pbInitBtn = document.getElementById("pb-init");
    const pbPreset  = document.getElementById("pb-preset");
    const pbName    = document.getElementById("pb-name");
    const pbPhone   = document.getElementById("pb-phone");
    const pbAdd     = document.getElementById("pb-add");
    const pbLookup  = document.getElementById("pb-lookup");
    const pbRemove  = document.getElementById("pb-remove");
    const pbOpCard  = document.getElementById("pb-op-card");
    const pbOpResult = document.getElementById("pb-op-result");
    const pbContacts = document.getElementById("pb-contacts");
    const pbStats   = document.getElementById("pb-stats");
    const pbTable   = document.getElementById("pb-table");

    function renderPhoneBookSnapshot(data) {
        // Stats
        const snap = data;
        renderStats(pbStats, [
            { label: "Table Size", value: snap.size },
            { label: "Entries", value: snap.count },
            { label: "Load Factor", value: snap.load_factor },
            { label: "Collisions", value: snap.collisions },
            { label: "Avg Chain", value: snap.avg_chain_length },
        ]);

        // Contacts list
        const entries = snap.entries || [];
        if (entries.length === 0) {
            pbContacts.innerHTML = '<p class="info">No contacts yet. Add some or load presets.</p>';
        } else {
            let chtml = '<div class="contacts-grid">';
            entries.forEach(e => {
                chtml += `<div class="contact-card">
                    <div class="contact-name">${e.name}</div>
                    <div class="contact-phone">${e.phone}</div>
                </div>`;
            });
            chtml += '</div>';
            pbContacts.innerHTML = chtml;
        }

        // Hash table internals
        let thtml = "";
        snap.buckets.forEach(bucket => {
            thtml += `<div class="bucket-row">`;
            thtml += `<div class="bucket-index">${bucket.index}</div>`;
            thtml += `<div class="bucket-content">`;
            if (bucket.entries.length === 0) {
                thtml += `<span class="bucket-empty">empty</span>`;
            } else {
                bucket.entries.forEach((entry, i) => {
                    if (i > 0) thtml += `<span class="chain-arrow">&#8594;</span>`;
                    thtml += `<span class="chain-node">${entry.key}: ${entry.value}</span>`;
                });
            }
            thtml += `</div></div>`;
        });
        pbTable.innerHTML = thtml;
    }

    function showPhoneBookOp(op) {
        if (!op) { pbOpCard.style.display = "none"; return; }
        pbOpCard.style.display = "";
        let text = "";
        if (op.action === "add") {
            text += `ADD: "${op.name}" -> "${op.phone}"\n`;
            const hi = op.hash_info;
            text += `Hash: ${hi.hash_computation}\n`;
            text += `Bucket: ${hi.hash_value}\n`;
            text += `Collision: ${hi.collision ? "YES" : "no"}\n`;
            if (hi.chain_length_after !== undefined) {
                text += `Chain length after: ${hi.chain_length_after}\n`;
            }
        } else if (op.action === "lookup") {
            text += `LOOKUP: "${op.name}"\n`;
            const hi = op.hash_info;
            text += `Hash: ${hi.hash_computation}\n`;
            text += `Bucket: ${hi.hash_value}\n`;
            text += `Probes: ${hi.probes}\n`;
            if (op.found) {
                text += `Result: FOUND -> "${op.phone}"\n`;
            } else {
                text += `Result: NOT FOUND\n`;
            }
        } else if (op.action === "remove") {
            text += `REMOVE: "${op.name}"\n`;
            const hi = op.hash_info;
            text += `Hash bucket: ${hi.hash_value}\n`;
            text += `Result: ${op.found ? "REMOVED" : "NOT FOUND"}\n`;
        }
        pbOpResult.textContent = text;
    }

    // Initialize phone book
    pbInitBtn.addEventListener("click", async () => {
        pbOpCard.style.display = "none";
        const data = await apiPost("/api/phonebook/init", {
            size: parseInt(pbSize.value) || 17,
        });
        renderPhoneBookSnapshot(data);
    });

    // Load presets
    pbPreset.addEventListener("click", async () => {
        const data = await apiPost("/api/phonebook/preset", {});
        renderPhoneBookSnapshot(data);
        pbOpCard.style.display = "";
        pbOpResult.textContent = "Loaded 10 preset contacts.\n\nInsert details:\n" +
            data.insert_results.map(r =>
                `  ${r.name} -> bucket[${r.hash_info.hash_value}]${r.hash_info.collision ? " (collision)" : ""}`
            ).join("\n");
    });

    // Phone book operations
    async function phoneBookOp(operation) {
        const body = {
            operation: operation,
            name: pbName.value.trim() || null,
            phone: pbPhone.value.trim() || null,
        };
        const data = await apiPost("/api/phonebook/op", body);
        if (data.error) { alert(data.error); return; }
        renderPhoneBookSnapshot(data);
        showPhoneBookOp(data.last_operation);
    }

    pbAdd.addEventListener("click", () => phoneBookOp("add"));
    pbLookup.addEventListener("click", () => phoneBookOp("lookup"));
    pbRemove.addEventListener("click", () => phoneBookOp("remove"));

    // Auto-init phone book
    pbInitBtn.click();


    // =================================================================
    // 4. PERFORMANCE COMPARISON
    // =================================================================
    const perfSizes    = document.getElementById("perf-sizes");
    const perfSearches = document.getElementById("perf-searches");
    const perfRunBtn   = document.getElementById("perf-run");
    const perfResult   = document.getElementById("perf-result");

    perfRunBtn.addEventListener("click", async () => {
        perfResult.innerHTML = '<div class="card"><span class="spinner"></span> Running benchmarks... this may take a moment for large N.</div>';
        const sizes = parseNumbers(perfSizes.value).filter(n => n > 0);
        const searchCount = parseInt(perfSearches.value) || 100;

        if (sizes.length === 0) {
            perfResult.innerHTML = '<div class="card">Please enter at least one data size.</div>';
            return;
        }

        const data = await apiPost("/api/performance/compare", {
            sizes: sizes,
            search_count: searchCount,
        });

        let html = "";

        // Results table
        html += `<div class="card">
            <h2>Benchmark Results</h2>
            <p class="info">${data.search_count} lookups per data size. Times in milliseconds.</p>
            <table class="cmp-table">
                <tr>
                    <th>N (data size)</th>
                    <th>Python dict (ms)</th>
                    <th>Custom Hash (ms)</th>
                    <th>List Search (ms)</th>
                    <th>Speedup (dict)</th>
                    <th>Speedup (custom)</th>
                </tr>`;
        data.results.forEach(r => {
            html += `<tr>
                <td><strong>${r.n.toLocaleString()}</strong></td>
                <td>${r.hash_table_ms}</td>
                <td>${r.custom_hash_ms}</td>
                <td>${r.list_search_ms}</td>
                <td><span class="tag tag-green">${r.speedup_builtin}x</span></td>
                <td><span class="tag tag-blue">${r.speedup_custom}x</span></td>
            </tr>`;
        });
        html += `</table>
            <p class="info" style="margin-top:0.75rem">${data.note}</p>
        </div>`;

        // Bar chart: List search time vs hash table time
        const maxListTime = Math.max(...data.results.map(r => r.list_search_ms), 0.001);

        html += `<div class="card">
            <h2>Lookup Time by Data Size</h2>
            <p class="info">Comparing time to perform ${data.search_count} lookups at each N.</p>`;

        data.results.forEach(r => {
            html += `<h3>N = ${r.n.toLocaleString()}</h3>
            <div class="bar-chart">
                <div class="bar-row">
                    <span class="bar-label">Python dict</span>
                    <div class="bar-track"><div class="bar-fill c0" style="width:${pct(r.hash_table_ms, maxListTime)}%"></div></div>
                    <span class="bar-value">${r.hash_table_ms} ms</span>
                </div>
                <div class="bar-row">
                    <span class="bar-label">Custom Hash</span>
                    <div class="bar-track"><div class="bar-fill c2" style="width:${pct(r.custom_hash_ms, maxListTime)}%"></div></div>
                    <span class="bar-value">${r.custom_hash_ms} ms</span>
                </div>
                <div class="bar-row">
                    <span class="bar-label">List Search</span>
                    <div class="bar-track"><div class="bar-fill c4" style="width:${pct(r.list_search_ms, maxListTime)}%"></div></div>
                    <span class="bar-value">${r.list_search_ms} ms</span>
                </div>
            </div>`;
        });
        html += `</div>`;

        // Speedup chart
        html += `<div class="card">
            <h2>Speedup: Hash Table over Linear Search</h2>
            <p class="info">How many times faster the hash table is compared to list linear search.</p>
            <div class="bar-chart">`;
        const maxSpeedup = Math.max(...data.results.map(r =>
            typeof r.speedup_builtin === "number" ? r.speedup_builtin : 0
        ), 1);
        data.results.forEach(r => {
            const su = typeof r.speedup_builtin === "number" ? r.speedup_builtin : 0;
            html += `<div class="bar-row">
                <span class="bar-label">N=${r.n.toLocaleString()}</span>
                <div class="bar-track"><div class="bar-fill c0" style="width:${pct(su, maxSpeedup)}%"></div></div>
                <span class="bar-value">${r.speedup_builtin}x faster</span>
            </div>`;
        });
        html += `</div></div>`;

        // Educational note
        html += `<div class="card">
            <h2>Why is Hash Table O(1)?</h2>
            <p>A hash table computes the bucket index directly from the key using a hash
               function. Regardless of how many elements are stored (N), the lookup
               involves:</p>
            <ol style="margin:0.75rem 0 0.75rem 1.5rem">
                <li>Compute hash(key) -- constant time</li>
                <li>Go to bucket[hash % size] -- constant time</li>
                <li>Check a few entries in that bucket (ideally 1) -- constant on average</li>
            </ol>
            <p>In contrast, a list must scan elements one by one until it finds the target,
               taking O(n) time on average. As N grows, the list slows down linearly while
               the hash table stays fast.</p>
            <p style="margin-top:0.5rem">The "Custom Hash" column shows our hand-built chaining hash table.
               It is slower than Python's built-in <code>dict</code> (which uses a highly
               optimized C implementation) but still dramatically faster than linear search
               for large N.</p>
        </div>`;

        perfResult.innerHTML = html;
    });

});
