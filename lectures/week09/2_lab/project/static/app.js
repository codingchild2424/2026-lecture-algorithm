/* ======================================================================
   Algorithm Review Web App -- Frontend Logic
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
    // 1. SORTING
    // -----------------------------------------------------------------
    const sortInput     = document.getElementById("sort-input");
    const sortAlgo      = document.getElementById("sort-algo");
    const sortRunBtn    = document.getElementById("sort-run");
    const sortCompBtn   = document.getElementById("sort-compare");
    const sortResult    = document.getElementById("sort-result");
    const sortRandom    = document.getElementById("sort-random");

    sortRandom.addEventListener("click", () => {
        const size = 20;
        const arr = Array.from({ length: size }, () => Math.floor(Math.random() * 200) - 50);
        sortInput.value = arr.join(", ");
    });

    sortRunBtn.addEventListener("click", async () => {
        const numbers = parseNumbers(sortInput.value);
        if (numbers.length === 0) { sortResult.textContent = "Please enter some numbers."; return; }
        sortResult.innerHTML = '<span class="spinner"></span> Sorting...';
        const data = await apiPost("/api/sort", { numbers, algorithm: sortAlgo.value });
        if (data.error) { sortResult.textContent = data.error; return; }
        let html = `Algorithm : ${data.algorithm}\n`;
        html += `Input size: ${data.input_size}\n`;
        html += `Sorted    : [${data.sorted.join(", ")}]\n`;
        html += `Comparisons: ${data.comparisons}\n`;
        html += `Swaps      : ${data.swaps}\n`;
        html += `Time       : ${data.time_ms} ms\n\n`;
        html += `--- Steps (${data.steps.length}) ---\n`;
        data.steps.slice(0, 40).forEach((s, i) => {
            if (s.action === "swap") {
                html += `${i + 1}. Swap indices [${s.indices}] -> [${s.array.join(", ")}]\n`;
            } else if (s.action === "insert") {
                html += `${i + 1}. Insert ${s.value} at index ${s.index} -> [${s.array.join(", ")}]\n`;
            } else if (s.action === "merge") {
                html += `${i + 1}. Merge [${s.left.join(",")}] + [${s.right.join(",")}] -> [${s.merged.join(",")}]\n`;
            } else if (s.action === "partition") {
                html += `${i + 1}. Partition pivot=${s.pivot} at index ${s.pivot_index} -> [${s.array.join(", ")}]\n`;
            }
        });
        if (data.steps.length > 40) html += `... and ${data.steps.length - 40} more steps\n`;
        sortResult.textContent = html;
    });

    // -- Comparison view --
    const sortCmpResult = document.getElementById("sort-cmp-result");

    sortCompBtn.addEventListener("click", async () => {
        const numbers = parseNumbers(sortInput.value);
        if (numbers.length === 0) { sortCmpResult.innerHTML = "Please enter some numbers."; return; }
        sortCmpResult.innerHTML = '<span class="spinner"></span> Comparing all algorithms...';
        const data = await apiPost("/api/sort/compare", { numbers, algorithm: "all" });
        let html = `<table class="cmp-table">
            <tr><th>Algorithm</th><th>Comparisons</th><th>Swaps</th><th>Time (ms)</th></tr>`;
        const names = Object.keys(data.results);
        const maxTime = Math.max(...names.map(n => data.results[n].time_ms), 0.001);
        names.forEach(name => {
            const r = data.results[name];
            html += `<tr>
                <td style="text-transform:capitalize;font-weight:600">${name}</td>
                <td>${r.comparisons}</td>
                <td>${r.swaps}</td>
                <td>${r.time_ms}</td>
            </tr>`;
        });
        html += `</table>`;

        // Bar chart for time
        html += `<h3>Time Comparison</h3><div class="bar-chart">`;
        names.forEach((name, i) => {
            const r = data.results[name];
            const pct = Math.max((r.time_ms / maxTime) * 100, 1);
            html += `<div class="bar-row">
                <span class="bar-label">${name}</span>
                <div class="bar-track"><div class="bar-fill c${i}" style="width:${pct}%"></div></div>
                <span class="bar-value">${r.time_ms} ms</span>
            </div>`;
        });
        html += `</div>`;

        // Bar chart for comparisons
        const maxCmp = Math.max(...names.map(n => data.results[n].comparisons), 1);
        html += `<h3>Comparisons</h3><div class="bar-chart">`;
        names.forEach((name, i) => {
            const r = data.results[name];
            const pct = Math.max((r.comparisons / maxCmp) * 100, 1);
            html += `<div class="bar-row">
                <span class="bar-label">${name}</span>
                <div class="bar-track"><div class="bar-fill c${i}" style="width:${pct}%"></div></div>
                <span class="bar-value">${r.comparisons}</span>
            </div>`;
        });
        html += `</div>`;

        sortCmpResult.innerHTML = html;
    });

    // -----------------------------------------------------------------
    // 2. BINARY SEARCH
    // -----------------------------------------------------------------
    const bsInput   = document.getElementById("bs-input");
    const bsTarget  = document.getElementById("bs-target");
    const bsRunBtn  = document.getElementById("bs-run");
    const bsResult  = document.getElementById("bs-result");
    const bsRandom  = document.getElementById("bs-random");

    bsRandom.addEventListener("click", () => {
        const size = 20;
        const arr = Array.from({ length: size }, () => Math.floor(Math.random() * 100));
        arr.sort((a, b) => a - b);
        bsInput.value = arr.join(", ");
        bsTarget.value = arr[Math.floor(Math.random() * size)];
    });

    bsRunBtn.addEventListener("click", async () => {
        const numbers = parseNumbers(bsInput.value);
        const target = Number(bsTarget.value);
        if (numbers.length === 0 || isNaN(target)) {
            bsResult.innerHTML = "Please enter numbers and a target.";
            return;
        }
        bsResult.innerHTML = '<span class="spinner"></span> Searching...';
        const data = await apiPost("/api/search/binary", { numbers, target });

        let html = `<p><strong>Sorted array:</strong> [${data.sorted_array.join(", ")}]</p>`;
        html += `<p><strong>Target:</strong> ${target}</p>`;
        html += `<p><strong>Result:</strong> `;
        if (data.found) {
            html += `<span class="tag tag-green">FOUND</span> at index ${data.index}`;
        } else {
            html += `<span class="tag tag-red">NOT FOUND</span>`;
        }
        html += `</p>`;
        html += `<p><strong>Steps taken:</strong> ${data.total_steps} (max for this size: ${data.max_possible_steps})</p>`;
        html += `<p class="info">Binary search complexity: O(log n) = O(log ${data.sorted_array.length}) ~ ${data.max_possible_steps} steps max</p>`;
        html += `<h3>Search Steps</h3><ol class="steps-list">`;

        data.steps.forEach(s => {
            if (s.action === "found") {
                html += `<li class="found">Check index ${s.mid} (value ${s.mid_value}) -- <strong>Found!</strong> [low=${s.low}, high=${s.high}]</li>`;
            } else if (s.action === "go_right") {
                html += `<li>Check index ${s.mid} (value ${s.mid_value}) -- too small, search right [low=${s.low}, high=${s.high}]</li>`;
            } else if (s.action === "go_left") {
                html += `<li>Check index ${s.mid} (value ${s.mid_value}) -- too large, search left [low=${s.low}, high=${s.high}]</li>`;
            } else if (s.action === "not_found") {
                html += `<li class="not-found">Search space exhausted -- target not in array</li>`;
            }
        });
        html += `</ol>`;
        bsResult.innerHTML = html;
    });

    // -----------------------------------------------------------------
    // 3. GREEDY -- Coin Change
    // -----------------------------------------------------------------
    const greedyAmount = document.getElementById("greedy-amount");
    const greedyCoins  = document.getElementById("greedy-coins");
    const greedyRunBtn = document.getElementById("greedy-run");
    const greedyResult = document.getElementById("greedy-result");

    greedyRunBtn.addEventListener("click", async () => {
        const amount = parseInt(greedyAmount.value);
        const coins  = parseNumbers(greedyCoins.value).filter(n => n > 0);
        if (isNaN(amount) || amount <= 0 || coins.length === 0) {
            greedyResult.innerHTML = "Please enter a positive amount and coin denominations.";
            return;
        }
        greedyResult.innerHTML = '<span class="spinner"></span> Calculating...';
        const data = await apiPost("/api/greedy/coins", { amount, coins });

        let html = `<p><strong>Amount:</strong> ${amount}</p>`;
        html += `<p><strong>Available coins:</strong> [${coins.join(", ")}]</p>`;
        if (data.success) {
            html += `<p><span class="tag tag-green">SUCCESS</span> Total coins used: <strong>${data.total_coins}</strong></p>`;
        } else {
            html += `<p><span class="tag tag-amber">PARTIAL</span> Could not make exact change. Remaining: ${data.remaining}</p>`;
        }
        html += `<h3>Greedy Steps</h3><ol class="steps-list">`;
        data.steps.forEach(s => {
            html += `<li>Use coin <strong>${s.coin}</strong> x ${s.count} (remaining: ${s.remaining_before} -> ${s.remaining_after})</li>`;
        });
        html += `</ol>`;
        html += `<p class="info">${data.note}</p>`;
        html += `<h3>Coins Used</h3><div class="items-grid">`;
        data.coins_used.forEach(c => {
            html += `<div class="item-card selected">${c.coin} x ${c.count} = ${c.coin * c.count}</div>`;
        });
        html += `</div>`;
        greedyResult.innerHTML = html;
    });

    // -----------------------------------------------------------------
    // 4a. DP -- Fibonacci
    // -----------------------------------------------------------------
    const fibN       = document.getElementById("fib-n");
    const fibRunBtn  = document.getElementById("fib-run");
    const fibResult  = document.getElementById("fib-result");

    fibRunBtn.addEventListener("click", async () => {
        const n = parseInt(fibN.value);
        if (isNaN(n) || n < 0 || n > 35) {
            fibResult.innerHTML = "Please enter n between 0 and 35.";
            return;
        }
        fibResult.innerHTML = '<span class="spinner"></span> Computing...';
        const data = await apiPost("/api/dp/fibonacci", { n });

        let html = `<p><strong>F(${data.n}) = ${data.dp.value}</strong></p>`;
        html += `<table class="cmp-table">
            <tr><th>Method</th><th>Function Calls</th><th>Time (ms)</th><th>Complexity</th></tr>
            <tr>
                <td><strong>Naive Recursion</strong></td>
                <td>${data.naive.calls.toLocaleString()}</td>
                <td>${data.naive.time_ms}</td>
                <td><span class="tag tag-red">${data.naive.complexity}</span></td>
            </tr>
            <tr>
                <td><strong>DP (Bottom-Up)</strong></td>
                <td>${data.dp.calls.toLocaleString()}</td>
                <td>${data.dp.time_ms}</td>
                <td><span class="tag tag-green">${data.dp.complexity}</span></td>
            </tr>
        </table>`;
        if (data.speedup !== "N/A") {
            html += `<p style="margin-top:0.75rem"><strong>Speedup:</strong> DP is ~<strong>${data.speedup}x</strong> faster</p>`;
        }

        // Bar chart: calls comparison
        const maxCalls = Math.max(data.naive.calls, data.dp.calls, 1);
        html += `<h3>Function Calls Comparison</h3><div class="bar-chart">`;
        html += `<div class="bar-row">
            <span class="bar-label">Naive</span>
            <div class="bar-track"><div class="bar-fill c4" style="width:${(data.naive.calls / maxCalls) * 100}%"></div></div>
            <span class="bar-value">${data.naive.calls.toLocaleString()}</span>
        </div>`;
        html += `<div class="bar-row">
            <span class="bar-label">DP</span>
            <div class="bar-track"><div class="bar-fill c2" style="width:${(data.dp.calls / maxCalls) * 100}%"></div></div>
            <span class="bar-value">${data.dp.calls.toLocaleString()}</span>
        </div>`;
        html += `</div>`;

        // DP table
        if (data.dp.table && data.dp.table.length <= 40) {
            html += `<h3>DP Table Build-Up</h3><div class="result-area">`;
            data.dp.table.forEach(entry => {
                html += `F(${entry.index}) = ${entry.value}\n`;
            });
            html += `</div>`;
        }

        fibResult.innerHTML = html;
    });

    // -----------------------------------------------------------------
    // 4b. DP -- Knapsack
    // -----------------------------------------------------------------
    const ksCapacity  = document.getElementById("ks-capacity");
    const ksItems     = document.getElementById("ks-items");
    const ksRunBtn    = document.getElementById("ks-run");
    const ksResult    = document.getElementById("ks-result");
    const ksPreset    = document.getElementById("ks-preset");

    ksPreset.addEventListener("click", () => {
        ksCapacity.value = "15";
        ksItems.value = "Laptop,5,10\nHeadphones,3,7\nBook,2,4\nWater,1,2\nSnack,1,1\nTablet,4,8\nCharger,2,3";
    });

    ksRunBtn.addEventListener("click", async () => {
        const capacity = parseInt(ksCapacity.value);
        if (isNaN(capacity) || capacity <= 0) {
            ksResult.innerHTML = "Please enter a valid capacity.";
            return;
        }

        const lines = ksItems.value.trim().split("\n").filter(l => l.trim());
        const names = [], weights = [], values = [];
        for (const line of lines) {
            const parts = line.split(",").map(s => s.trim());
            if (parts.length >= 3) {
                names.push(parts[0]);
                weights.push(parseInt(parts[1]));
                values.push(parseInt(parts[2]));
            }
        }

        if (names.length === 0) {
            ksResult.innerHTML = "Please enter items in the format: name,weight,value (one per line).";
            return;
        }

        ksResult.innerHTML = '<span class="spinner"></span> Solving knapsack...';
        const data = await apiPost("/api/dp/knapsack", { capacity, weights, values, names });

        let html = `<p><strong>Capacity:</strong> ${capacity} | <strong>Items:</strong> ${names.length}</p>`;
        html += `<p><strong>Max value:</strong> <span class="tag tag-green">${data.max_value}</span> | `;
        html += `<strong>Weight used:</strong> ${data.total_weight} / ${capacity}</p>`;
        html += `<p class="info">DP table size: ${data.dp_table_size} | Complexity: ${data.complexity}</p>`;

        html += `<h3>All Items</h3><div class="items-grid">`;
        names.forEach((name, i) => {
            const isSelected = data.selected_items.some(s => s.name === name);
            html += `<div class="item-card${isSelected ? " selected" : ""}">
                <strong>${name}</strong><br>
                Weight: ${weights[i]} | Value: ${values[i]}
                ${isSelected ? '<br><span class="tag tag-green">SELECTED</span>' : ""}
            </div>`;
        });
        html += `</div>`;

        html += `<h3>Selected Items</h3><table class="cmp-table">
            <tr><th>Item</th><th>Weight</th><th>Value</th></tr>`;
        data.selected_items.forEach(item => {
            html += `<tr><td>${item.name}</td><td>${item.weight}</td><td>${item.value}</td></tr>`;
        });
        html += `<tr style="font-weight:700"><td>Total</td><td>${data.total_weight}</td><td>${data.max_value}</td></tr>`;
        html += `</table>`;

        ksResult.innerHTML = html;
    });
});
