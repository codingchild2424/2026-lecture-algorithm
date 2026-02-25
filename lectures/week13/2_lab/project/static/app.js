/* ======================================================================
   Algorithm Finale -- Frontend Logic
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

    async function apiGet(url) {
        const res = await fetch(url);
        return res.json();
    }

    const NS = "http://www.w3.org/2000/svg";


    // =================================================================
    // 1. TSP VISUALIZATION
    // =================================================================

    const tspSvg          = document.getElementById("tsp-svg");
    const tspSvgOptimal   = document.getElementById("tsp-svg-optimal");
    const tspSvgHeuristic = document.getElementById("tsp-svg-heuristic");
    const tspCityCount    = document.getElementById("tsp-city-count");
    const tspSolve        = document.getElementById("tsp-solve");
    const tspClear        = document.getElementById("tsp-clear");
    const tspStats        = document.getElementById("tsp-stats");
    const tspResult       = document.getElementById("tsp-result");
    const tspOptimalInfo  = document.getElementById("tsp-optimal-info");
    const tspHeuristicInfo = document.getElementById("tsp-heuristic-info");

    let tspCities = [];
    let tspCityCounter = 0;

    function renderTSPCanvas(svg, cities, tours) {
        svg.innerHTML = "";

        // Background click area
        const bg = document.createElementNS(NS, "rect");
        bg.setAttribute("width", "600");
        bg.setAttribute("height", "500");
        bg.setAttribute("fill", "transparent");
        bg.setAttribute("class", "tsp-clickable");
        svg.appendChild(bg);

        // Draw tours
        if (tours) {
            for (const tour of tours) {
                if (!tour.order || tour.order.length < 2) continue;
                const path = document.createElementNS(NS, "polygon");
                const points = tour.order.map(i => `${cities[i].x},${cities[i].y}`).join(" ");
                path.setAttribute("points", points);
                path.setAttribute("class", tour.cssClass || "tsp-tour-optimal");
                svg.appendChild(path);
            }
        }

        // Draw cities
        cities.forEach((city, idx) => {
            const g = document.createElementNS(NS, "g");
            g.setAttribute("class", "tsp-city");

            const circle = document.createElementNS(NS, "circle");
            circle.setAttribute("cx", city.x);
            circle.setAttribute("cy", city.y);
            circle.setAttribute("r", 14);
            g.appendChild(circle);

            const text = document.createElementNS(NS, "text");
            text.setAttribute("x", city.x);
            text.setAttribute("y", city.y);
            text.textContent = city.name || String(idx);
            g.appendChild(text);

            svg.appendChild(g);
        });
    }

    function updateTSPCount() {
        tspCityCount.textContent = `Cities: ${tspCities.length}`;
    }

    function refreshTSPMain() {
        renderTSPCanvas(tspSvg, tspCities, null);
        updateTSPCount();
        // Clear side panels
        renderTSPCanvas(tspSvgOptimal, [], null);
        renderTSPCanvas(tspSvgHeuristic, [], null);
        tspStats.innerHTML = "";
        tspResult.textContent = "";
        tspOptimalInfo.textContent = "";
        tspHeuristicInfo.textContent = "";
    }

    // Click to add city on main SVG
    tspSvg.addEventListener("click", (e) => {
        const rect = tspSvg.getBoundingClientRect();
        const svgWidth = tspSvg.viewBox.baseVal.width;
        const svgHeight = tspSvg.viewBox.baseVal.height;
        const scaleX = svgWidth / rect.width;
        const scaleY = svgHeight / rect.height;
        const x = Math.round((e.clientX - rect.left) * scaleX);
        const y = Math.round((e.clientY - rect.top) * scaleY);

        // Don't add if too close to edge
        if (x < 10 || x > 590 || y < 10 || y > 490) return;

        tspCities.push({ x, y, name: `C${tspCityCounter++}` });
        refreshTSPMain();
    });

    // Preset buttons
    document.getElementById("tsp-preset-pentagon").addEventListener("click", async () => {
        const data = await apiPost("/api/tsp/preset", { preset: "pentagon" });
        tspCities = data.cities;
        tspCityCounter = tspCities.length;
        refreshTSPMain();
    });

    document.getElementById("tsp-preset-random7").addEventListener("click", async () => {
        const data = await apiPost("/api/tsp/preset", { preset: "random_7" });
        tspCities = data.cities;
        tspCityCounter = tspCities.length;
        refreshTSPMain();
    });

    document.getElementById("tsp-preset-cluster8").addEventListener("click", async () => {
        const data = await apiPost("/api/tsp/preset", { preset: "cluster_8" });
        tspCities = data.cities;
        tspCityCounter = tspCities.length;
        refreshTSPMain();
    });

    tspClear.addEventListener("click", () => {
        tspCities = [];
        tspCityCounter = 0;
        refreshTSPMain();
    });

    // Solve TSP
    tspSolve.addEventListener("click", async () => {
        if (tspCities.length < 3) {
            alert("Place at least 3 cities to solve TSP.");
            return;
        }
        tspSolve.disabled = true;
        tspSolve.textContent = "Solving...";

        const data = await apiPost("/api/tsp/solve", { cities: tspCities });

        tspSolve.disabled = false;
        tspSolve.textContent = "Solve TSP";

        const nn = data.nearest_neighbor;
        const bf = data.brute_force;

        // Main canvas with both tours
        const mainTours = [];
        if (bf) {
            mainTours.push({ order: bf.order, cssClass: "tsp-tour-optimal" });
        }
        mainTours.push({ order: nn.order, cssClass: "tsp-tour-heuristic" });
        renderTSPCanvas(tspSvg, tspCities, mainTours);

        // Optimal tour side panel
        if (bf) {
            renderTSPCanvas(tspSvgOptimal, tspCities, [
                { order: bf.order, cssClass: "tsp-tour-optimal" }
            ]);
            const route = bf.order.map(i => tspCities[i].name).join(" -> ") +
                          " -> " + tspCities[bf.order[0]].name;
            tspOptimalInfo.textContent =
                `Distance: ${bf.distance}\n` +
                `Time: ${bf.time_ms} ms\n` +
                `Permutations checked: ${bf.permutations_checked.toLocaleString()}\n` +
                `Route: ${route}`;
        } else {
            renderTSPCanvas(tspSvgOptimal, tspCities, null);
            tspOptimalInfo.textContent = data.brute_force_skipped || "N too large for brute force.";
        }

        // Heuristic tour side panel
        renderTSPCanvas(tspSvgHeuristic, tspCities, [
            { order: nn.order, cssClass: "tsp-tour-heuristic" }
        ]);
        const nnRoute = nn.order.map(i => tspCities[i].name).join(" -> ") +
                        " -> " + tspCities[nn.order[0]].name;
        tspHeuristicInfo.textContent =
            `Distance: ${nn.distance}\n` +
            `Time: ${nn.time_ms} ms\n` +
            `Route: ${nnRoute}`;

        // Stats
        if (bf) {
            const cmp = data.comparison;
            tspStats.innerHTML = `
                <div class="stat-box">
                    <div class="stat-value">${data.n}</div>
                    <div class="stat-label">Cities</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">${cmp.optimal_distance}</div>
                    <div class="stat-label">Optimal Distance</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">${cmp.heuristic_distance}</div>
                    <div class="stat-label">Heuristic Distance</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">${cmp.quality_percent}%</div>
                    <div class="stat-label">Heuristic Quality</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">${cmp.ratio}x</div>
                    <div class="stat-label">Ratio (NN / Opt)</div>
                </div>
            `;

            tspResult.textContent =
                `=== Brute Force (Exact) ===\n` +
                `Distance: ${bf.distance}\n` +
                `Time: ${bf.time_ms} ms\n` +
                `Permutations: ${bf.permutations_checked.toLocaleString()}\n\n` +
                `=== Nearest Neighbor (Heuristic) ===\n` +
                `Distance: ${nn.distance}\n` +
                `Time: ${nn.time_ms} ms\n\n` +
                `=== Comparison ===\n` +
                `The heuristic tour is ${cmp.ratio}x the optimal.\n` +
                `Quality: ${cmp.quality_percent}% of optimal.\n` +
                (bf.time_ms > 0 ? `Speed-up: ${(bf.time_ms / Math.max(nn.time_ms, 0.0001)).toFixed(1)}x faster with heuristic.` : "");
        } else {
            tspStats.innerHTML = `
                <div class="stat-box">
                    <div class="stat-value">${data.n}</div>
                    <div class="stat-label">Cities</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">${nn.distance}</div>
                    <div class="stat-label">Heuristic Distance</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value">${nn.time_ms} ms</div>
                    <div class="stat-label">Heuristic Time</div>
                </div>
            `;
            tspResult.textContent =
                (data.brute_force_skipped || "") + "\n\n" +
                `=== Nearest Neighbor (Heuristic) ===\n` +
                `Distance: ${nn.distance}\nTime: ${nn.time_ms} ms`;
        }
    });

    // Initialize with a preset
    (async () => {
        const data = await apiPost("/api/tsp/preset", { preset: "pentagon" });
        tspCities = data.cities;
        tspCityCounter = tspCities.length;
        refreshTSPMain();
    })();


    // =================================================================
    // 2. 0-1 KNAPSACK
    // =================================================================

    const ksCapacity  = document.getElementById("ks-capacity");
    const ksItemsBody = document.getElementById("ks-items-body");
    const ksAddItem   = document.getElementById("ks-add-item");
    const ksSolve     = document.getElementById("ks-solve");
    const ksStats     = document.getElementById("ks-stats");
    const ksSelected  = document.getElementById("ks-selected");
    const ksDPWrap    = document.getElementById("ks-dp-table-wrap");
    const ksPerfWrap  = document.getElementById("ks-perf-table-wrap");

    let ksItems = [];

    function renderKSItemsTable() {
        ksItemsBody.innerHTML = "";
        ksItems.forEach((item, idx) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${idx + 1}</td>
                <td><input type="text" class="ks-item-name" data-idx="${idx}" value="${item.name}" /></td>
                <td><input type="number" class="ks-item-weight" data-idx="${idx}" value="${item.weight}" min="1" /></td>
                <td><input type="number" class="ks-item-value" data-idx="${idx}" value="${item.value}" min="1" /></td>
                <td><button class="btn-remove" data-idx="${idx}">Remove</button></td>
            `;
            ksItemsBody.appendChild(tr);
        });

        // Attach change listeners
        document.querySelectorAll(".ks-item-name").forEach(el => {
            el.addEventListener("change", (e) => {
                ksItems[+e.target.dataset.idx].name = e.target.value;
            });
        });
        document.querySelectorAll(".ks-item-weight").forEach(el => {
            el.addEventListener("change", (e) => {
                ksItems[+e.target.dataset.idx].weight = parseInt(e.target.value) || 1;
            });
        });
        document.querySelectorAll(".ks-item-value").forEach(el => {
            el.addEventListener("change", (e) => {
                ksItems[+e.target.dataset.idx].value = parseInt(e.target.value) || 1;
            });
        });
        document.querySelectorAll(".btn-remove").forEach(el => {
            el.addEventListener("click", (e) => {
                ksItems.splice(+e.target.dataset.idx, 1);
                renderKSItemsTable();
            });
        });
    }

    ksAddItem.addEventListener("click", () => {
        const idx = ksItems.length + 1;
        ksItems.push({ name: `Item ${idx}`, weight: 2, value: 10 });
        renderKSItemsTable();
    });

    // Preset buttons
    async function loadKSPreset(preset) {
        const data = await apiPost("/api/knapsack/preset", { preset });
        if (data.error) { alert(data.error); return; }
        ksItems = data.items.map(it => ({ ...it }));
        ksCapacity.value = data.capacity;
        renderKSItemsTable();
        // Clear previous results
        ksStats.innerHTML = "";
        ksSelected.textContent = "";
        ksDPWrap.innerHTML = "";
        ksPerfWrap.innerHTML = "";
    }

    document.getElementById("ks-preset-small").addEventListener("click", () => loadKSPreset("small"));
    document.getElementById("ks-preset-medium").addEventListener("click", () => loadKSPreset("medium"));
    document.getElementById("ks-preset-large").addEventListener("click", () => loadKSPreset("large"));

    // Solve Knapsack
    ksSolve.addEventListener("click", async () => {
        if (ksItems.length === 0) {
            alert("Add items or load a preset first.");
            return;
        }
        const capacity = parseInt(ksCapacity.value) || 7;

        ksSolve.disabled = true;
        ksSolve.textContent = "Solving...";

        const data = await apiPost("/api/knapsack/solve", { items: ksItems, capacity });

        ksSolve.disabled = false;
        ksSolve.textContent = "Solve Knapsack";

        const dp = data.dp;
        const bf = data.brute_force;
        const cmp = data.comparison;

        // Stats
        ksStats.innerHTML = `
            <div class="stat-box">
                <div class="stat-value">${data.n}</div>
                <div class="stat-label">Items</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">${capacity}</div>
                <div class="stat-label">Capacity</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">${dp.max_value}</div>
                <div class="stat-label">Max Value</div>
            </div>
            <div class="stat-box">
                <div class="stat-value">${dp.selected.length}</div>
                <div class="stat-label">Items Selected</div>
            </div>
        `;

        // Selected items
        const selectedItems = dp.selected.map(i => data.items[i]);
        const totalWeight = selectedItems.reduce((s, it) => s + it.weight, 0);
        let selectedText = `Optimal Value: ${dp.max_value}\n`;
        selectedText += `Total Weight: ${totalWeight} / ${capacity}\n\n`;
        selectedText += `Selected Items:\n`;
        selectedItems.forEach(it => {
            selectedText += `  ${it.name} (w=${it.weight}, v=${it.value})\n`;
        });
        ksSelected.textContent = selectedText;

        // DP Table
        renderDPTable(dp.dp_table, data.items, capacity, dp.selected);

        // Performance comparison
        let perfHTML = `<table class="cmp-table">
            <thead><tr>
                <th>Metric</th>
                <th>Dynamic Programming</th>
                <th>Brute Force</th>
            </tr></thead><tbody>
            <tr>
                <td>Time (ms)</td>
                <td class="winner">${cmp.dp_time_ms}</td>
                <td>${cmp.bf_time_ms !== null ? cmp.bf_time_ms : "skipped"}</td>
            </tr>
            <tr>
                <td>Subproblems / Subsets</td>
                <td>${cmp.dp_subproblems.toLocaleString()}</td>
                <td>${cmp.bf_subsets !== null ? cmp.bf_subsets.toLocaleString() : "2^" + data.n}</td>
            </tr>
            <tr>
                <td>Time Complexity</td>
                <td><span class="tag tag-green">O(nW) = O(${data.n} * ${capacity})</span></td>
                <td><span class="tag tag-red">O(2^n) = O(2^${data.n})</span></td>
            </tr>
            <tr>
                <td>Optimal Value</td>
                <td>${dp.max_value}</td>
                <td>${bf ? bf.max_value : "N/A"}</td>
            </tr>
        </tbody></table>`;
        ksPerfWrap.innerHTML = perfHTML;
    });

    function renderDPTable(dpTable, items, capacity, selectedIndices) {
        const n = items.length;

        // Build the backtrack path for highlighting
        const backtrackCells = new Set();
        let w = capacity;
        for (let i = n; i >= 1; i--) {
            backtrackCells.add(`${i}-${w}`);
            if (dpTable[i][w] !== dpTable[i - 1][w]) {
                w -= items[i - 1].weight;
            }
        }
        backtrackCells.add(`0-${w}`);

        // Selected cells (where item was picked)
        const selectedCells = new Set();
        w = capacity;
        for (let i = n; i >= 1; i--) {
            if (dpTable[i][w] !== dpTable[i - 1][w]) {
                selectedCells.add(`${i}-${w}`);
                w -= items[i - 1].weight;
            }
        }

        let html = '<table class="dp-table"><thead><tr>';
        html += '<th class="corner">Item \\ W</th>';
        for (let ww = 0; ww <= capacity; ww++) {
            html += `<th>${ww}</th>`;
        }
        html += '</tr></thead><tbody>';

        for (let i = 0; i <= n; i++) {
            html += '<tr>';
            const rowLabel = i === 0 ? "0 (none)" : `${i} (${items[i - 1].name})`;
            html += `<th class="row-header">${rowLabel}</th>`;
            for (let ww = 0; ww <= capacity; ww++) {
                const key = `${i}-${ww}`;
                let cls = "";
                if (selectedCells.has(key)) {
                    cls = "dp-selected";
                } else if (backtrackCells.has(key)) {
                    cls = "dp-highlight";
                }
                html += `<td class="${cls}">${dpTable[i][ww]}</td>`;
            }
            html += '</tr>';
        }

        html += '</tbody></table>';
        ksDPWrap.innerHTML = html;
    }

    // Auto-load small preset
    loadKSPreset("small");


    // =================================================================
    // 3. ALGORITHM COMPLEXITY DASHBOARD
    // =================================================================

    const dashContent = document.getElementById("dash-content");
    const dashFilterBtns = document.querySelectorAll(".dash-filter-btn");
    let dashData = null;

    async function loadDashboard() {
        const data = await apiGet("/api/dashboard");
        dashData = data.categories;
        renderDashboard("all");
    }

    function renderDashboard(filter) {
        if (!dashData) return;
        let html = "";

        for (const category of dashData) {
            if (filter !== "all" && category.category !== filter) continue;

            html += `<div class="card dash-category">`;
            html += `<div class="dash-category-title">${category.category}</div>`;
            html += `<div class="dash-algo-grid">`;

            for (const algo of category.algorithms) {
                const paradigmTag = getParadigmTag(algo.paradigm);
                const stableTag = algo.stable !== undefined
                    ? (algo.stable ? '<span class="tag tag-green">Stable</span>' : '<span class="tag tag-gray">Unstable</span>')
                    : "";

                html += `
                    <div class="dash-algo-card">
                        <div class="algo-name">${algo.name}</div>
                        <div class="algo-detail">
                            <strong>Best:</strong> ${algo.best}<br>
                            <strong>Average:</strong> ${algo.average}<br>
                            <strong>Worst:</strong> ${algo.worst}<br>
                            <strong>Space:</strong> ${algo.space}<br>
                            <div style="margin-top:0.4rem">
                                ${paradigmTag} ${stableTag}
                                <span class="tag tag-gray">Week ${algo.week}</span>
                            </div>
                        </div>
                    </div>
                `;
            }

            html += `</div></div>`;
        }

        dashContent.innerHTML = html;
    }

    function getParadigmTag(paradigm) {
        const map = {
            "Brute Force": "tag-red",
            "Incremental": "tag-amber",
            "Divide & Conquer": "tag-blue",
            "Selection (Heap)": "tag-purple",
            "Non-comparison": "tag-purple",
            "Hashing": "tag-green",
            "Exploration": "tag-blue",
            "Greedy": "tag-green",
            "Dynamic Programming": "tag-amber",
            "DFS-based": "tag-blue",
            "Exhaustive Search": "tag-red",
            "Greedy Heuristic": "tag-amber",
        };
        const cls = map[paradigm] || "tag-gray";
        return `<span class="tag ${cls}">${paradigm}</span>`;
    }

    dashFilterBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            dashFilterBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            renderDashboard(btn.dataset.filter);
        });
    });

    loadDashboard();


    // =================================================================
    // 4. INTERACTIVE QUIZ
    // =================================================================

    const quizQuestionsDiv = document.getElementById("quiz-questions");
    const quizSubmit       = document.getElementById("quiz-submit");
    const quizReset        = document.getElementById("quiz-reset");
    const quizResultCard   = document.getElementById("quiz-result-card");
    const quizScore        = document.getElementById("quiz-score");
    const quizResults      = document.getElementById("quiz-results");

    let quizData = null;

    async function loadQuiz() {
        const data = await apiGet("/api/quiz");
        quizData = data;
        renderQuiz(data.questions);
    }

    function renderQuiz(questions) {
        let html = "";
        questions.forEach((q, idx) => {
            html += `
                <div class="quiz-question-card" id="quiz-q-${q.id}">
                    <div class="q-number">Question ${idx + 1} of ${questions.length}</div>
                    <div class="q-text">${q.question}</div>
                    <ul class="quiz-options">
            `;
            q.options.forEach((opt, oi) => {
                html += `
                    <li>
                        <label id="quiz-label-${q.id}-${oi}">
                            <input type="radio" name="quiz-${q.id}" value="${oi}" />
                            ${opt}
                        </label>
                    </li>
                `;
            });
            html += `
                    </ul>
                    <div class="quiz-explanation" id="quiz-exp-${q.id}"></div>
                </div>
            `;
        });
        quizQuestionsDiv.innerHTML = html;
    }

    quizSubmit.addEventListener("click", async () => {
        if (!quizData) return;

        // Gather answers
        const answers = [];
        for (const q of quizData.questions) {
            const selected = document.querySelector(`input[name="quiz-${q.id}"]:checked`);
            answers.push(selected ? parseInt(selected.value) : -1);
        }

        // Check if all answered
        const unanswered = answers.filter(a => a === -1).length;
        if (unanswered > 0) {
            if (!confirm(`You have ${unanswered} unanswered question(s). Submit anyway?`)) return;
        }

        const data = await apiPost("/api/quiz/submit", { answers });

        // Disable all radio buttons
        document.querySelectorAll('#quiz-questions input[type="radio"]').forEach(el => {
            el.disabled = true;
        });

        // Show results on each question
        data.results.forEach(r => {
            r.options.forEach((opt, oi) => {
                const label = document.getElementById(`quiz-label-${r.id}-${oi}`);
                if (!label) return;
                if (oi === r.correct_answer) {
                    label.classList.add("correct-answer");
                    if (r.user_answer === oi) {
                        label.classList.add("correct");
                    }
                } else if (r.user_answer === oi && !r.is_correct) {
                    label.classList.add("incorrect");
                }
            });

            // Show explanation
            const expEl = document.getElementById(`quiz-exp-${r.id}`);
            if (expEl) {
                expEl.textContent = (r.is_correct ? "Correct! " : "Incorrect. ") + r.explanation;
                expEl.classList.add("visible");
            }
        });

        // Score summary
        quizResultCard.style.display = "block";
        const pct = data.percentage;
        let circleClass = "poor";
        if (pct >= 90) circleClass = "excellent";
        else if (pct >= 70) circleClass = "good";
        else if (pct >= 50) circleClass = "needs-work";

        quizScore.innerHTML = `
            <div style="flex:1; text-align:center">
                <div class="quiz-score-circle ${circleClass}">
                    ${data.score}/${data.total}
                </div>
                <div style="font-size:1.1rem; font-weight:700; color:var(--primary-dark)">${pct}%</div>
                <div class="info">${getScoreMessage(pct)}</div>
            </div>
        `;

        quizSubmit.style.display = "none";
        quizReset.style.display = "inline-flex";

        // Scroll to results
        quizResultCard.scrollIntoView({ behavior: "smooth", block: "start" });
    });

    function getScoreMessage(pct) {
        if (pct === 100) return "Perfect score! You have mastered the algorithms.";
        if (pct >= 90) return "Excellent! You have a strong understanding of algorithms.";
        if (pct >= 70) return "Good job! A few topics to review.";
        if (pct >= 50) return "Not bad, but there is room for improvement.";
        return "Keep studying! Review the course material and try again.";
    }

    quizReset.addEventListener("click", () => {
        quizResultCard.style.display = "none";
        quizSubmit.style.display = "inline-flex";
        quizReset.style.display = "none";
        loadQuiz();
    });

    loadQuiz();

});
