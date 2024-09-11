"use client";

import { useState } from "react";
import Head from "next/head";
import styles from "./page.module.css";
import RenderMap from "./components/RenderMap.js";
import '../node_modules/@fortawesome/fontawesome-free/css/all.min.css';

export default function Home() {
    const [data, setData] = useState(null);
    const [inputURL, setInputURL] = useState('');
    const [userPrompt, setUserPrompt] = useState('');
    const [pageSummary, setPageSummary] = useState('');

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        if (name === "inputURL") {
            setInputURL(value);
        } else if (name === "userPrompt") {
            setUserPrompt(value);
        }
    };

    const handleURLClick = (url) => {
        setInputURL(url);
    };

    const isValidURL = (url) => {
        try {
            new URL(url);
            return true;
        } catch (_) {
            // Try adding http:// and check again
            try {
                new URL(`http://${url}`);
                return true;
            } catch (_) {
                return false;
            }
        }
    };

    const openURLInNewTab = (url) => {
        window.open(`http://${url}`, '_blank', 'noopener,noreferrer');
    };
    /*
    const handleSubmit = (event) => {
        event.preventDefault();
        if (isValidURL(inputURL)) {
            try {
                // Simulate an API call with a timeout
                setTimeout(() => {
                    const response = {
                        page_summary: "Full Page Summary of the given URL",
                        name: "main topic name",
                        text: "main text",
                        sub_topics: [
                            {
                                name: "first topic",
                                text: "text",
                                sub_topics: [
                                    {
                                        name: "first sub topic",
                                        text: "First sub topic text"
                                    },
                                    {
                                        name: "second sub topic",
                                        text: "Second sub topic text"
                                    },
                                    {
                                        name: "third sub topic",
                                        text: "Third sub topic text"
                                    }
                                ]
                            },
                            {
                                name: "Second topic",
                                text: "text",
                                sub_topics: [
                                    {
                                        name: "Second First sub topic",
                                        text: "Second First sub topic text"
                                    },
                                    {
                                        name: "Second second sub topic",
                                        text: "Second second topic text"
                                    },
                                    {
                                        name: "Second Third sub topic",
                                        text: "Second Third topic text"
                                    }
                                ]
                            }
                        ],
                        URLS: [
                            "www.Microsoft.com",
                            "www.Google.com",
                            "www.AWS.com"
                        ]
                    };

                    // Set the data and page summary states
                    setData(response);
                    setPageSummary(response.page_summary);
                }, 1000); // Simulate a 1-second delay
            } catch (error) {
                console.error("An error occurred:", error);
                setPageSummary("An error occurred while fetching data.");
            }
        } else {
            console.error("Invalid URL");
            setPageSummary("The provided URL is invalid.");
        }
    };
    */

   const handleSubmit = async (event) => {
    event.preventDefault();

    if (isValidURL(inputURL)) {
        try {
            // Make the API call
            const response = await fetch('http://127.0.0.1:5001/get_mindmap_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: inputURL,
                    user_prompt: userPrompt
                }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            console.log(response);
            const data_ = await response.json();
            const data = JSON.parse(data_);
            console.log(data);
            // Set the data and page summary states
            setData(data);
            setPageSummary(data.page_summary);
        } catch (error) {
            console.error('An error occurred:', error);
            setPageSummary('An error occurred while fetching data.');
        }
    } else {
        console.error('Invalid URL');
        setPageSummary('The provided URL is invalid.');
    }
};


    return (
        <div className={styles.container}>
            <Head>
                <title>Mind Map Input</title>
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
            <div className={styles.inputRow}>
                <textarea className={styles.textarea}
                    name="inputURL"
                    value={inputURL}
                    onChange={handleInputChange}
                    placeholder="Enter url here..."
                ></textarea>
                <textarea className={styles.textarea}
                    name="userPrompt"
                    value={userPrompt}
                    onChange={handleInputChange}
                    placeholder="Enter prompt here..."
                ></textarea>
                <button className={styles.button} type="submit" onClick={handleSubmit}>Render Mind Map</button>
            </div>
            {data && data.URLS && (
                <div className={styles.urlBox}>
                    <h2>Related URLs</h2>
                    <ul>
                        {data.URLS.map((url, index) => (
                            <li key={index}>
                                <a
                                    href={`http://${url}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    onClick={(e) => {
                                        e.preventDefault();
                                        handleURLClick(url);
                                    }}
                                >
                                    <i onClick={() => openURLInNewTab(url)} className="fas fa-external-link-alt"></i>
                                    {url}
                                </a>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
            {pageSummary && (
                <div className={styles.pageSummary}>
                    <h2>Page Summary</h2>
                    <p>{pageSummary}</p>
                </div>
            )}
            <div className={styles.mapSection}>
                {data && <RenderMap data={data} />}
            </div>
        </div>
    );
}