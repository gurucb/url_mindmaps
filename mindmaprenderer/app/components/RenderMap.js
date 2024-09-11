"use client";

import { useEffect } from "react";
import { useState } from 'react';
import * as d3 from "d3";
import Head from "next/head";
export default function RenderMap({ data }) {
    useEffect(() => {

        console.log(data);
        console.log("useEffect is running");

        // Clear any existing SVG content
        d3.select("#mindmap-svg").selectAll("*").remove();

        const margin = { top: 20, right: 120, bottom: 20, left: 120 };
        const height = window.innerHeight - margin.top - margin.bottom;
        const width = window.innerWidth; // Initial width for SVG

        // Create SVG container
        const svg = d3
            .select("#mindmap-svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const tree = d3.tree().size([height, width / 2]);

        const root = d3.hierarchy(data, d => d.sub_topics);

        tree(root);

        // Calculate SVG width dynamically based on the content
        // const svgWidth = Math.max(...root.descendants().map(d => d.y)) + margin.right + 100; // Add extra margin
        d3.select("#mindmap-svg").attr("width", window.innerWidth);

        const colorScale = d3.scaleOrdinal(d3.schemeSet3);

        // Tooltip div
        const tooltip = d3.select("#mindmap")
            .append("div")
            .attr("class", "tooltip")
            .style("opacity", 0);


        // Draw links
        const link = svg
            .selectAll(".link")
            .data(root.descendants().slice(1))
            .enter()
            .append("path")
            .attr("class", "link")
            .attr("d", (d) => `
                M${d.y},${d.x}
                C${(d.y + d.parent.y) / 2},${d.x}
                ${(d.y + d.parent.y) / 2},${d.parent.x}
                ${d.parent.y},${d.parent.x}
            `)
            .style("fill", "none")
            .style("stroke", "#ccc")
            .style("stroke-width", "2px")

        // Draw nodes
        const node = svg
            .selectAll(".node")
            .data(root.descendants())
            .enter()
            .append("g")
            .attr("class", "node")
            .attr("transform", (d) => `translate(${d.y},${d.x})`)
            .on("click", (event, d) => {
                if (d.data.link) {
                    window.open(d.data.link, "_blank");
                }
            })
            .on("mouseover", (event, d) => {
                tooltip.transition().duration(200).style("opacity", .9);
                tooltip.html(d.data.text)
                    .style("left", `${event.pageX + 5}px`)
                    .style("top", `${event.pageY - 28}px`);
            })
            .on("mouseout", () => {
                tooltip.transition().duration(500).style("opacity", 0);
            });

        // Add circle background for nodes
        node.append("circle")
            .attr("r", 15)
            .style("fill", (d) => colorScale(d.depth))
            .style("stroke", "#000")
            .style("stroke-width", "0.5px");

        const linkIconBase64 = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICA8cGF0aCBkPSJNMTIgNGwtMi0yTDYuOTUgMTMuOTZMMjAuMyA2Ljc1bDEuMjUgMS4yNWwxLjI1LTEuMjVMMi4yMCA4LjUsNCAxNiIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtY29sb3I9IiMzMzMiLz48L3N2Zz4=";

        // Add URL icon for nodes with a link
        node
            .filter((d) => d.data.link)
            .append("svg:image")
            .attr("xlink:href", linkIconBase64)
            .attr("width", 20) // Adjust size if necessary
            .attr("height", 20) // Adjust size if necessary
            .attr("x", -15) // Adjust positioning if necessary
            .attr("y", -40) // Move the icon slightly above the node
            .style("cursor", "pointer")
            .on("click", (event, d) => {
                if (d.data.link) window.open(d.data.link, "_blank");
            });

        // Add text
        const text = node
            .append("text")
            .attr("dy", "0.35em")
            .attr("x", (d) => (d.children ? -20 : 20))
            .style("text-anchor", (d) => (d.children ? "end" : "start"))
            .style("font", "20px sans-serif")
            .style("font-weight", "bolder")
            //.style("fill", "#fff")
            //.style("stroke", "#000") // Add black outline
            //.style("stroke-width", "1px") 
            //.style("text-shadow", "1px 1px 2px rgba(0, 0, 0, 0.5)")
            .text((d) => d.data.name)
            .each(function (d) {
                const bbox = this.getBBox();
                const nodeColor = colorScale(d.depth);
                function getContrastYIQ(hexcolor) {
                    hexcolor = hexcolor.replace("#", "");
                    const r = parseInt(hexcolor.substr(0, 2), 16);
                    const g = parseInt(hexcolor.substr(2, 2), 16);
                    const b = parseInt(hexcolor.substr(4, 2), 16);
                    const yiq = (r * 299 + g * 587 + b * 114) / 1000;
                    return yiq >= 128 ? "#333333" : "white";
                }

                const textColor = getContrastYIQ(nodeColor);

                d3.select(this)
                    .style("fill", textColor);
                ///.style("stroke", textColor === "white" ? "#000" : "#fff");

                if (textColor !== "#333333") {
                    d3.select(this).style("text-shadow", "1px 1px 2px rgba(0, 0, 0, 0.5)");
                };

                if (d.depth < 2) {
                    d3.select(this.parentNode).insert("rect", ":first-child")
                        .attr("x", bbox.x - 10)
                        .attr("y", bbox.y - 15)
                        .attr("width", bbox.width + 20)
                        .attr("height", bbox.height + 30)
                        .attr("rx", 10) // Rounded edges
                        .attr("ry", 10) // Rounded edges
                        .style("fill", nodeColor)
                        .style("stroke", "#495057")
                        .style("stroke-width", "1px")
                        .style("box-shadow", "0 4px 8px rgba(0, 0, 0, 0.1)");
                }
            });


        node
            .append("title")
            .text((d) => d.data.text);

        // Zoom and pan functionality
        const zoom = d3.zoom()
            .scaleExtent([0.5, 2])
            .on("zoom", (event) => {
                svg.attr("transform", event.transform);
            });

        d3.select("#mindmap-svg").call(zoom);

        console.log("Mind map created");

    }, [data]);
    return (
        <main>
            <Head>
                <title>Mind Map</title>
                <style>
                    {`
                    .tooltip {
                        position: absolute;
                        text-align: center;
                        padding: 10px;
                        font: 12px sans-serif;
                        background: rgba(0, 0, 0, 0.8);
                        color: white;
                        border-radius: 4px;
                        pointer-events: none;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                        max-width: 300px;
                        word-wrap: break-word;
                    }

                    .scroll-container {
                        width: 100%;
                        height: 100vh;
                        overflow: auto;
                        position: relative;
                    }

                    svg {
                        display: block;
                        height: 100%;
                        width: auto; /* Adjust width based on content */
                    }
                    `}
                </style>
            </Head>
            <div className="scroll-container">
                <svg id="mindmap-svg"></svg>
            </div>
        </main>
    );
}
