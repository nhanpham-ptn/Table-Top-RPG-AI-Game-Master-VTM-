import React, {useEffect} from "react";
import { useNavigate } from "react-router-dom";
import Camarilla_Logo from './assets/Camarilla_Logo.png'
import "@fontsource/vt323";


export default function Loading() {
    const navigate = useNavigate();

    useEffect(() => {
    const interval = setInterval(async () => {
        const response = await fetch("http://localhost:5000/loading");
        const data = await response.json();

        if (data.lore) {
            clearInterval(interval);
            navigate("/gameplay");
        }
    }, 2000);

    return () => clearInterval(interval);
    }, []);

    return (
        <div
            className="
              terminal-font
              min-h-[600px]
              flex
              flex-col
              justify-center
              items-center
              bg-black
              text-green-400
              border-4
              border-green-500
              relative
              overflow-hidden
            "
            style={{
              backgroundImage: `url(${Camarilla_Logo})`,
              backgroundSize: "200px",
              backgroundRepeat: "no-repeat",
              backgroundPosition: "top right",
            }}
          >
          <div
                className="absolute inset-0 pointer-events-none opacity-10"
                style={{
                  background:
                    "repeating-linear-gradient(0deg, transparent 0px, transparent 2px, #22c55e 3px, transparent 4px)",
                }}
              />
            <h1
              className="
                text-7xl
                md:text-9xl
                mb-12
                tracking-[0.25em]
                text-center
                font-bold
                cursor 
              "
              style={{
                textShadow: `
                  0 0 5px #22c55e,
                  0 0 10px #22c55e,
                  0 0 25px #22c55e,
                  0 0 50px #22c55e
                `,
              }}
            >
              Loading....
            </h1>
        </div>
    )
}
