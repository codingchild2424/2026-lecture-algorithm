/* ======================================================================
   Graph Traversal Explorer -- Frontend Logic
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
    // Helper: parse edge list from text  (formats: "A-B", "A->B", "A B")
    // -----------------------------------------------------------------
    function parseEdges(text) {
        const edges = [];
        const parts = text.split(/[,\n]+/).map(s => s.trim()).filter(Boolean);
        for (const part of parts) {
            const m = part.match(/^(\S+)\s*[->\s]+\s*(\S+)$/);
            if (m) edges.push([m[1], m[2]]);
        }
        return edges;
    }

    function parseNodeList(text) {
        return text.split(/[\s,]+/).map(s => s.trim()).filter(Boolean);
    }

    // =================================================================
    // SVG Graph Rendering
    // =================================================================

    const NS = "http://www.w3.org/2000/svg";

    /**
     * Render a graph to an SVG element.
     *
     * @param {SVGElement} svg        - target SVG
     * @param {object}     graphData  - {nodes, edges, directed}
     * @param {object}     positions  - {nodeName: {x, y}}
     * @param {object}     opts       - optional highlight configuration
     *   opts.visitedNodes   - Set of visited node names
     *   opts.currentNode    - name of current node
     *   opts.pathNodes      - Set of nodes on the shortest path
     *   opts.pathEdges      - Set of "u->v" strings for path edges
     *   opts.treeEdges      - Set of "u->v" strings for BFS/DFS tree edges
     *   opts.cycleNodes     - Set of nodes in a detected cycle
     *   opts.cycleEdges     - Set of "u->v" strings for cycle edges
     *   opts.nodeClasses    - Map of nodeName -> extra CSS class
     *   opts.orderMap       - Map of nodeName -> visit order number
     */
    function renderGraph(svg, graphData, positions, opts = {}) {
        svg.innerHTML = "";

        const directed = graphData.directed;
        const nodeR = 22;

        // Arrowhead marker for directed edges
        if (directed) {
            const defs = document.createElementNS(NS, "defs");

            function makeMarker(id, color) {
                const marker = document.createElementNS(NS, "marker");
                marker.setAttribute("id", id);
                marker.setAttribute("viewBox", "0 0 10 10");
                marker.setAttribute("refX", "10");
                marker.setAttribute("refY", "5");
                marker.setAttribute("markerWidth", "8");
                marker.setAttribute("markerHeight", "8");
                marker.setAttribute("orient", "auto-start-reverse");
                const path = document.createElementNS(NS, "path");
                path.setAttribute("d", "M 0 0 L 10 5 L 0 10 z");
                path.setAttribute("fill", color);
                marker.appendChild(path);
                defs.appendChild(marker);
            }

            makeMarker("arrow-default", "#94a3b8");
            makeMarker("arrow-highlight", "#10b981");
            makeMarker("arrow-tree", "#818cf8");
            makeMarker("arrow-cycle", "#ef4444");
            svg.appendChild(defs);
        }

        const treeEdgeSet = opts.treeEdges || new Set();
        const pathEdgeSet = opts.pathEdges || new Set();
        const cycleEdgeSet = opts.cycleEdges || new Set();

        // Draw edges
        for (const edge of graphData.edges) {
            const u = edge.from || edge[0];
            const v = edge.to || edge[1];
            const pu = positions[u];
            const pv = positions[v];
            if (!pu || !pv) continue;

            // Shorten line so it does not overlap the node circle
            const dx = pv.x - pu.x;
            const dy = pv.y - pu.y;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const offset = directed ? nodeR + 10 : nodeR + 2;
            const ux = pu.x + (dx / dist) * (nodeR + 2);
            const uy = pu.y + (dy / dist) * (nodeR + 2);
            const vx = pv.x - (dx / dist) * offset;
            const vy = pv.y - (dy / dist) * offset;

            const line = document.createElementNS(NS, "line");
            line.setAttribute("x1", ux);
            line.setAttribute("y1", uy);
            line.setAttribute("x2", vx);
            line.setAttribute("y2", vy);

            let cls = "graph-edge";
            let markerEnd = directed ? "url(#arrow-default)" : "";

            const edgeKey = `${u}->${v}`;
            const edgeKeyRev = `${v}->${u}`;

            if (pathEdgeSet.has(edgeKey) || pathEdgeSet.has(edgeKeyRev)) {
                cls += " highlighted";
                markerEnd = directed ? "url(#arrow-highlight)" : "";
            } else if (cycleEdgeSet.has(edgeKey) || cycleEdgeSet.has(edgeKeyRev)) {
                cls += " cycle-edge";
                markerEnd = directed ? "url(#arrow-cycle)" : "";
            } else if (treeEdgeSet.has(edgeKey) || treeEdgeSet.has(edgeKeyRev)) {
                cls += " tree-edge";
                markerEnd = directed ? "url(#arrow-tree)" : "";
            }

            line.setAttribute("class", cls);
            if (markerEnd) line.setAttribute("marker-end", markerEnd);
            svg.appendChild(line);
        }

        // Draw nodes
        const visitedSet = opts.visitedNodes || new Set();
        const pathNodeSet = opts.pathNodes || new Set();
        const cycleNodeSet = opts.cycleNodes || new Set();
        const nodeClasses = opts.nodeClasses || {};
        const orderMap = opts.orderMap || {};

        for (const nodeName of graphData.nodes) {
            const pos = positions[nodeName];
            if (!pos) continue;

            const g = document.createElementNS(NS, "g");
            let cls = "graph-node";

            if (nodeClasses[nodeName]) {
                cls += " " + nodeClasses[nodeName];
            } else if (nodeName === opts.currentNode) {
                cls += " current";
            } else if (pathNodeSet.has(nodeName)) {
                cls += " path-node";
            } else if (cycleNodeSet.has(nodeName)) {
                cls += " cycle-node";
            } else if (visitedSet.has(nodeName)) {
                cls += " visited";
            }

            g.setAttribute("class", cls);

            const circle = document.createElementNS(NS, "circle");
            circle.setAttribute("cx", pos.x);
            circle.setAttribute("cy", pos.y);
            g.appendChild(circle);

            const text = document.createElementNS(NS, "text");
            text.setAttribute("x", pos.x);
            text.setAttribute("y", pos.y);
            text.textContent = nodeName;
            g.appendChild(text);

            svg.appendChild(g);

            // Visit order badge
            if (orderMap[nodeName] !== undefined) {
                const bx = pos.x + 16;
                const by = pos.y - 16;
                const bg = document.createElementNS(NS, "circle");
                bg.setAttribute("cx", bx);
                bg.setAttribute("cy", by);
                bg.setAttribute("r", 9);
                bg.setAttribute("class", "node-order-bg");
                svg.appendChild(bg);

                const bt = document.createElementNS(NS, "text");
                bt.setAttribute("x", bx);
                bt.setAttribute("y", by);
                bt.setAttribute("class", "node-order-badge");
                bt.setAttribute("text-anchor", "middle");
                bt.setAttribute("dominant-baseline", "central");
                bt.textContent = String(orderMap[nodeName] + 1);
                svg.appendChild(bt);
            }
        }
    }


    // =================================================================
    // 1. GRAPH TRAVERSAL (BFS / DFS)
    // =================================================================

    const travDirected = document.getElementById("trav-directed");
    const travNodes    = document.getElementById("trav-nodes");
    const travEdges    = document.getElementById("trav-edges");
    const travBuild    = document.getElementById("trav-build");
    const travPreset   = document.getElementById("trav-preset");
    const travAlgo     = document.getElementById("trav-algo");
    const travStart    = document.getElementById("trav-start");
    const travRun      = document.getElementById("trav-run");
    const travStepBack = document.getElementById("trav-step-back");
    const travStepFwd  = document.getElementById("trav-step-fwd");
    const travPlay     = document.getElementById("trav-play");
    const travStepInfo = document.getElementById("trav-step-info");
    const travSvg      = document.getElementById("trav-svg");
    const travOrder    = document.getElementById("trav-order");
    const travLog      = document.getElementById("trav-log");

    let travGraphData = null;
    let travPositions = null;
    let travResult = null;
    let travStepIdx = -1;
    let travPlayTimer = null;

    // Build graph from inputs
    travBuild.addEventListener("click", async () => {
        const nodes = parseNodeList(travNodes.value);
        const edges = parseEdges(travEdges.value);
        const directed = travDirected.value === "true";
        const data = await apiPost("/api/graph/init", { directed, nodes, edges });
        travGraphData = data.graph;
        travPositions = data.positions;
        travResult = null;
        travStepIdx = -1;
        resetTravControls();
        renderGraph(travSvg, travGraphData, travPositions);
        travOrder.textContent = "";
        travLog.textContent = "";
    });

    // Load preset
    travPreset.addEventListener("click", async () => {
        const data = await apiPost("/api/graph/preset", {});
        travGraphData = data.graph;
        travPositions = data.positions;
        travResult = null;
        travStepIdx = -1;
        resetTravControls();
        renderGraph(travSvg, travGraphData, travPositions);
        // Fill in the form for reference
        travDirected.value = String(data.graph.directed);
        travNodes.value = data.graph.nodes.join(", ");
        travEdges.value = data.graph.edges.map(e => `${e.from}-${e.to}`).join(", ");
        travOrder.textContent = "";
        travLog.textContent = "";
    });

    // Run traversal
    travRun.addEventListener("click", async () => {
        if (!travGraphData) { alert("Build or load a graph first."); return; }
        const start = travStart.value.trim() || travGraphData.nodes[0] || "";
        const algo = travAlgo.value;
        const data = await apiPost("/api/graph/traverse", { algorithm: algo, start });
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }
        travGraphData = data.graph;
        travPositions = data.positions;
        travResult = data.result;
        travStepIdx = -1;
        enableTravControls();
        renderGraph(travSvg, travGraphData, travPositions);

        // Show full result
        travOrder.textContent =
            `Algorithm: ${travResult.algorithm}\n` +
            `Start: ${travResult.start}\n` +
            `Visit order: ${travResult.visit_order.join(" -> ")}\n`;

        // Log
        let logText = "";
        travResult.steps.forEach((s, i) => {
            logText += `Step ${i + 1}: visit ${s.node}`;
            if (s.level !== undefined) logText += ` (level ${s.level})`;
            if (s.enqueued) logText += ` | enqueued: [${s.enqueued.join(", ")}]`;
            if (s.pushed) logText += ` | pushed: [${s.pushed.join(", ")}]`;
            if (s.queue) logText += ` | queue: [${s.queue.join(", ")}]`;
            if (s.stack) logText += ` | stack: [${s.stack.join(", ")}]`;
            logText += "\n";
        });
        travLog.textContent = logText;
    });

    function resetTravControls() {
        travStepBack.disabled = true;
        travStepFwd.disabled = true;
        travPlay.disabled = true;
        travStepInfo.textContent = "";
        clearInterval(travPlayTimer);
        travPlayTimer = null;
    }

    function enableTravControls() {
        travStepFwd.disabled = false;
        travPlay.disabled = false;
        travStepBack.disabled = true;
        travStepInfo.textContent = "Step 0 / " + travResult.steps.length;
    }

    function renderTravStep() {
        if (!travResult) return;
        const steps = travResult.steps;
        const visited = new Set();
        const orderMap = {};
        let current = null;

        for (let i = 0; i <= travStepIdx && i < steps.length; i++) {
            visited.add(steps[i].node);
            orderMap[steps[i].node] = i;
        }
        if (travStepIdx >= 0 && travStepIdx < steps.length) {
            current = steps[travStepIdx].node;
        }

        const treeEdges = new Set(
            travResult.tree_edges.map(e => `${e.from}->${e.to}`)
        );

        renderGraph(travSvg, travGraphData, travPositions, {
            visitedNodes: visited,
            currentNode: current,
            treeEdges: treeEdges,
            orderMap: orderMap,
        });

        travStepBack.disabled = travStepIdx < 0;
        travStepFwd.disabled = travStepIdx >= steps.length - 1;
        travStepInfo.textContent = `Step ${travStepIdx + 1} / ${steps.length}`;
    }

    travStepFwd.addEventListener("click", () => {
        if (!travResult) return;
        if (travStepIdx < travResult.steps.length - 1) {
            travStepIdx++;
            renderTravStep();
        }
    });

    travStepBack.addEventListener("click", () => {
        if (!travResult) return;
        if (travStepIdx >= 0) {
            travStepIdx--;
            renderTravStep();
        }
    });

    travPlay.addEventListener("click", () => {
        if (!travResult) return;
        if (travPlayTimer) {
            clearInterval(travPlayTimer);
            travPlayTimer = null;
            travPlay.textContent = "Play";
            return;
        }
        travPlay.textContent = "Pause";
        // Reset if already at the end
        if (travStepIdx >= travResult.steps.length - 1) {
            travStepIdx = -1;
            renderGraph(travSvg, travGraphData, travPositions);
        }
        travPlayTimer = setInterval(() => {
            if (travStepIdx < travResult.steps.length - 1) {
                travStepIdx++;
                renderTravStep();
            } else {
                clearInterval(travPlayTimer);
                travPlayTimer = null;
                travPlay.textContent = "Play";
            }
        }, 700);
    });

    // Auto-load preset on page load
    travPreset.click();


    // =================================================================
    // 2. BFS SHORTEST PATH
    // =================================================================

    const spStart  = document.getElementById("sp-start");
    const spEnd    = document.getElementById("sp-end");
    const spRun    = document.getElementById("sp-run");
    const spSvg    = document.getElementById("sp-svg");
    const spResult = document.getElementById("sp-result");

    spRun.addEventListener("click", async () => {
        if (!travGraphData) {
            alert("Build or load a graph in the Traversal tab first.");
            return;
        }
        const start = spStart.value.trim();
        const end = spEnd.value.trim();
        if (!start || !end) { alert("Enter both start and end nodes."); return; }

        const data = await apiPost("/api/graph/shortest-path", { start, end });
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }

        const result = data.result;
        const pathNodes = new Set(result.path || []);
        const pathEdges = new Set();
        if (result.path) {
            for (let i = 0; i < result.path.length - 1; i++) {
                pathEdges.add(`${result.path[i]}->${result.path[i + 1]}`);
                pathEdges.add(`${result.path[i + 1]}->${result.path[i]}`);
            }
        }

        const nodeClasses = {};
        if (result.found) {
            nodeClasses[start] = "start-node";
            nodeClasses[end] = "end-node";
        }

        renderGraph(spSvg, data.graph, data.positions, {
            pathNodes,
            pathEdges,
            nodeClasses,
        });

        if (result.found) {
            spResult.textContent =
                `Path found!\n` +
                `Distance: ${result.distance} edge(s)\n` +
                `Path: ${result.path.join(" -> ")}\n\n` +
                `BFS explored ${result.steps.length} node(s) to find this path.`;
        } else {
            spResult.textContent =
                `No path found from ${start} to ${end}.\n` +
                `BFS explored ${result.steps.length} node(s).`;
        }
    });


    // =================================================================
    // 3. TOPOLOGICAL SORT / CYCLE DETECTION
    // =================================================================

    const dagNodes       = document.getElementById("dag-nodes");
    const dagEdges       = document.getElementById("dag-edges");
    const dagBuild       = document.getElementById("dag-build");
    const dagPresetDag   = document.getElementById("dag-preset-dag");
    const dagPresetCycle = document.getElementById("dag-preset-cycle");
    const dagToposort    = document.getElementById("dag-toposort");
    const dagCycle       = document.getElementById("dag-cycle");
    const dagSvg         = document.getElementById("dag-svg");
    const dagResult      = document.getElementById("dag-result");
    const dagLog         = document.getElementById("dag-log");

    let dagGraphData = null;
    let dagPositions = null;

    dagBuild.addEventListener("click", async () => {
        const nodes = parseNodeList(dagNodes.value);
        const edges = parseEdges(dagEdges.value);
        const data = await apiPost("/api/dag/init", { nodes, edges });
        dagGraphData = data.graph;
        dagPositions = data.positions;
        renderGraph(dagSvg, dagGraphData, dagPositions);
        dagResult.textContent = "";
        dagLog.textContent = "";
    });

    dagPresetDag.addEventListener("click", async () => {
        const data = await apiPost("/api/dag/preset-dag", {});
        dagGraphData = data.graph;
        dagPositions = data.positions;
        dagNodes.value = data.graph.nodes.join(", ");
        dagEdges.value = data.graph.edges.map(e => `${e.from}-${e.to}`).join(", ");
        renderGraph(dagSvg, dagGraphData, dagPositions);
        dagResult.textContent = "";
        dagLog.textContent = "";
    });

    dagPresetCycle.addEventListener("click", async () => {
        const data = await apiPost("/api/dag/preset-cycle", {});
        dagGraphData = data.graph;
        dagPositions = data.positions;
        dagNodes.value = data.graph.nodes.join(", ");
        dagEdges.value = data.graph.edges.map(e => `${e.from}-${e.to}`).join(", ");
        renderGraph(dagSvg, dagGraphData, dagPositions);
        dagResult.textContent = "";
        dagLog.textContent = "";
    });

    dagToposort.addEventListener("click", async () => {
        if (!dagGraphData) { alert("Build a directed graph first."); return; }
        const data = await apiPost("/api/dag/toposort", {});
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }

        const result = data.result;
        const orderMap = {};
        result.order.forEach((n, i) => { orderMap[n] = i; });

        renderGraph(dagSvg, data.graph, data.positions, {
            visitedNodes: new Set(result.order),
            orderMap,
        });

        if (result.has_cycle) {
            dagResult.textContent =
                `Topological sort FAILED -- the graph contains a cycle.\n` +
                `Processed ${result.processed} out of ${result.total_nodes} nodes.\n` +
                `Remaining nodes are part of or depend on a cycle.`;
        } else {
            dagResult.textContent =
                `Topological order:\n` +
                result.order.map((n, i) => `  ${i + 1}. ${n}`).join("\n") +
                `\n\nAll ${result.total_nodes} nodes processed. No cycle detected.`;
        }

        // Log
        let logText = "";
        result.steps.forEach((s, i) => {
            logText += `Step ${i + 1}: remove ${s.node}`;
            if (s.reduced && s.reduced.length > 0) {
                logText += ` | reduced: ${s.reduced.map(r => `${r.node}(in=${r.new_in_degree})`).join(", ")}`;
            }
            if (s.newly_zero) {
                logText += ` | newly zero: [${s.newly_zero.join(", ")}]`;
            }
            logText += "\n";
        });
        dagLog.textContent = logText;
    });

    dagCycle.addEventListener("click", async () => {
        if (!dagGraphData) { alert("Build a directed graph first."); return; }
        const data = await apiPost("/api/dag/cycle", {});
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }

        const result = data.result;
        const cycleNodes = new Set(result.cycle || []);
        const cycleEdges = new Set();
        if (result.cycle && result.cycle.length > 1) {
            for (let i = 0; i < result.cycle.length - 1; i++) {
                cycleEdges.add(`${result.cycle[i]}->${result.cycle[i + 1]}`);
            }
        }

        renderGraph(dagSvg, data.graph, data.positions, {
            cycleNodes,
            cycleEdges,
        });

        if (result.has_cycle) {
            dagResult.textContent =
                `Cycle DETECTED!\n` +
                `Cycle: ${result.cycle.join(" -> ")}\n\n` +
                `DFS found a back edge, confirming a cycle exists in the graph.`;
        } else {
            dagResult.textContent =
                `No cycle detected.\n` +
                `The graph is a DAG (Directed Acyclic Graph). Topological sort is possible.`;
        }

        // Log
        let logText = "";
        result.steps.forEach((s, i) => {
            if (s.action === "enter") {
                logText += `${i + 1}. Enter ${s.node} (mark GRAY)\n`;
            } else if (s.action === "finish") {
                logText += `${i + 1}. Finish ${s.node} (mark BLACK)\n`;
            } else if (s.action === "back_edge") {
                logText += `${i + 1}. BACK EDGE: ${s.from} -> ${s.to} (CYCLE!)\n`;
            }
        });
        dagLog.textContent = logText;
    });


    // =================================================================
    // 4. SOCIAL NETWORK
    // =================================================================

    const socUser    = document.getElementById("soc-user");
    const socDepth   = document.getElementById("soc-depth");
    const socRun     = document.getElementById("soc-run");
    const socInit    = document.getElementById("soc-init");
    const socSvg     = document.getElementById("soc-svg");
    const socFriends = document.getElementById("soc-friends");
    const socSuggestions = document.getElementById("soc-suggestions");
    const socLog     = document.getElementById("soc-log");

    let socGraphData = null;
    let socPositions = null;

    socInit.addEventListener("click", async () => {
        const data = await apiPost("/api/social/init", {});
        socGraphData = data.graph;
        socPositions = data.positions;

        // Populate user dropdown
        socUser.innerHTML = "";
        data.users.forEach(u => {
            const opt = document.createElement("option");
            opt.value = u;
            opt.textContent = u;
            socUser.appendChild(opt);
        });

        renderGraph(socSvg, socGraphData, socPositions);
        socFriends.textContent = "Select a user and click 'Find Suggestions'.";
        socSuggestions.innerHTML = "";
        socLog.textContent = "";
    });

    socRun.addEventListener("click", async () => {
        if (!socGraphData) { alert("Load the social network first."); return; }
        const user = socUser.value;
        const depth = parseInt(socDepth.value) || 2;
        if (!user) { alert("Select a user."); return; }

        const data = await apiPost("/api/social/suggest", { user, depth });
        if (data.error || (data.result && data.result.error)) {
            alert(data.error || data.result.error);
            return;
        }

        const result = data.result;
        const directFriends = new Set(result.direct_friends);
        const suggestions = new Set(result.suggestions.map(s => s.person));

        // Build node classes
        const nodeClasses = {};
        nodeClasses[user] = "user-node";
        for (const f of directFriends) nodeClasses[f] = "friend-node";
        for (const s of suggestions) {
            if (!nodeClasses[s]) nodeClasses[s] = "suggestion";
        }

        // BFS tree edges
        const treeEdges = new Set(
            result.bfs_tree.tree_edges.map(e => `${e.from}->${e.to}`)
        );

        renderGraph(socSvg, data.graph, data.positions, {
            nodeClasses,
            treeEdges,
        });

        // Direct friends
        socFriends.textContent =
            `${user}'s friends: ${result.direct_friends.join(", ")}`;

        // Suggestions
        if (result.suggestions.length === 0) {
            socSuggestions.innerHTML =
                '<p class="info">No new friend suggestions at this depth.</p>';
        } else {
            let html = '<div class="suggestions-grid">';
            result.suggestions.forEach(s => {
                html += `<div class="suggestion-card">
                    <div class="sug-name">${s.person}</div>
                    <div class="sug-detail">
                        <span class="tag tag-blue">${s.distance} hop(s)</span>
                        via: ${s.via_path.join(" -> ")}
                    </div>
                </div>`;
            });
            html += '</div>';
            socSuggestions.innerHTML = html;
        }

        // Log
        let logText = "";
        result.steps.forEach((s, i) => {
            logText += `Step ${i + 1}: visit ${s.node} (level ${s.level})`;
            if (s.enqueued) logText += ` | enqueued: [${s.enqueued.join(", ")}]`;
            logText += "\n";
        });
        socLog.textContent = logText;
    });

    // Auto-load social network
    socInit.click();

});
