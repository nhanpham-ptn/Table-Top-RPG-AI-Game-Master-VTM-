import React from "react";
import { useNavigate } from "react-router-dom";
import Camarilla_Logo from './assets/Camarilla_Logo.png'
import "@fontsource/vt323";


export default function Start() {
    const navigate = useNavigate();

    const characterCreated  = async  () => {
        const response = await fetch("http://localhost:5000");

        const data = await response.json();
        return !data.redirect;
    };
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
              WELCOME, KINDRED
            </h1>
            <button
              onClick={
               async () => {
                const exist = await characterCreated()
                if (exist) {
                  navigate("/gameplay")
                }
                else {
                  navigate("/character")
                }
                
                }
              }
              className="
                text-4xl
                md:text-5xl

                px-12
                py-5

                border-4
                border-green-500

                tracking-[0.15em]

                hover:bg-green-500
                hover:text-black

                hover:shadow-[0_0_25px_rgba(34,197,94,0.9)]

                transition-all
                duration-200

                active:translate-y-[2px]
              "
            >
              &gt; REGISTER KINDRED
            </button>
        </div>
    )
}
