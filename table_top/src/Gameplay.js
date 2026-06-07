import React, { useState, useEffect } from "react";
import "@fontsource/vt323";



export default function Gameplay() {
    const [story, setStory] = useState("");
    const inputStyle =
        "bg-black border border-green-500 text-green-400 p-2 w-full focus:outline-none focus:ring-1 focus:ring-green-400";

    const received = async  () => {
        const response = await fetch("http://localhost:5000/gameplay");

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setStory(data.message);
        setInputVisible(true);
        return data.message
    };

    useEffect(() => {
        const loadStory = async () => {
            try {
            const text = await received();
            setStory(text);
            } catch (err) {
            console.error(err);
            }
        };

        loadStory();
        }, []);

    const [prompt, setPrompt] = useState("");
    const [inputVisible, setInputVisible] = useState(true);

    const sending = async () => {
        setInputVisible(false);
        setStory("");
        try {
            const response = await fetch("http://localhost:5000/gameplay", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    action: prompt,
                }),
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();

            setStory(data.message);
            setPrompt("");
            setInputVisible(true);
        } catch (err) {
            console.error(err);
            setInputVisible(true);
        }
    };

    return (
        <>
            <div
                className="
                   terminal-font 
                   min-h-[600px] 
                   flex flex-col 
                   justify-center 
                   items-center 
                   bg-black 
                   text-green-400 
                   border-4 
                   border-green-500 
                   relative 
                   overflow-hidden"

                style={{
                backgroundSize: "200px",
                backgroundRepeat: "no-repeat", 
                backgroundPosition: "top right", }} 
            >
                <div className="relative z-10 w-[80%] h-[70vh] border-2 border-green-500 p-4 overflow-y-auto mb-4">
                    <h3 className="whitespace-pre-wrap text-2xl">
                    {story}
                    </h3>
                </div>

                {inputVisible && (
                <div className="w-[80%] flex gap-2">
                    <input
                        placeholder="What would you do?"
                        className={inputStyle}
                        value={prompt}
                        onChange={(e) => setPrompt(e.target.value)}
                    />

                    <button
                        onClick={sending}
                        className="
                            border
                            border-green-500
                            px-4
                            hover:bg-green-500
                            hover:text-black
                        "
                    >
                        SEND
                    </button>
                </div>
            )}
                
            </div>

            
        </>
    )
}