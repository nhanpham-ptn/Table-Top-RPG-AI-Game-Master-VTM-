// make it like when an accountant is registering an account for you or in this case, you're signing up as a kindred
// I want to display each section horizontally like the character sheet
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import Camarilla_Logo from './assets/Camarilla_Logo.png'
import "@fontsource/vt323";


const inputStyle =
  "bg-black border border-green-500 text-green-400 p-2 w-full focus:outline-none focus:ring-1 focus:ring-green-400";

export default function CharacterCreator() {
  const navigate = useNavigate();

  const [character, setCharacter] = useState({
    name: "",
    concept: "",
    predator: "Alleycat",

    sire: "",
    generation: 13,
    age: 0,

    ambition: "",
    desire: "",

    clan: "",

    health: 10,
    humanity: 10,
    blood_potency: 5,

    attributes: {
      physical: {
        strength: 1,
        dexterity: 1,
        stamina: 1
      },

      social: {
        charisma: 1,
        manipulation: 1,
        composure: 1
      },

      mental: {
        intelligence: 1,
        wits: 1,
        resolve: 1
      }
    },

    skills: {
      physical: {
        athletics: 0,
        brawl: 0,
        craft: 0,
        drive: 0,
        firearms: 0,
        larceny: 0,
        melee: 0,
        stealth: 0,
        survival: 0
      },

      social: {
        animal_ken: 0,
        etiquette: 0,
        insight: 0,
        intimidation: 0,
        leadership: 0,
        performance: 0,
        persuasion: 0,
        streetwise: 0,
        subterfuge: 0
      },

      mental: {
        academics: 0,
        awareness: 0,
        finance: 0,
        investigation: 0,
        medicine: 0,
        occult: 0,
        politics: 0,
        science: 0,
        technology: 0
      }
    },

    disciplines: {},

    items: {},

    advantages: {},

    disadvantages: {}
  });
  async function submitCharacter() {
      try {
        const response = await fetch("http://localhost:5000/character", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(character),
        });

        navigate("/gameplay")

      } catch (err) {

        console.error(err);

      }
  }

  const updateField = (field, value) => {
    setCharacter({ ...character, [field]: value });
  };

  const updateNested = (group, category, field, value) => {
    setCharacter({
      ...character,
      [group]: {
        ...character[group],
        [category]: {
          ...character[group][category],
          [field]: value
        }
      }
    });
  };

  const updateDiscipline = (name, value) => {
    setCharacter({
      ...character,
      disciplines: {
        ...character.disciplines,
        [name]: value
      }
    });
  };

  const updateAdvantage = (name, value) => {
    setCharacter({
      ...character,
      advantages: {
        ...character.advantages,
        [name]: value
      }
    });
  }

  const updateDisadvantage = (name, value) => {
    setCharacter({
      ...character,
      disadvantages: {
        ...character.disadvantages,
        [name]: value
      }
    });
  }
  return (
    <div className="p-6 max-w-6xl mx-auto bg-black text-green-400 font-mono"
          style={{
            backgroundImage: `url(${Camarilla_Logo})`,
            backgroundSize: "200px",
            backgroundRepeat: "no-repeat",
            backgroundPosition: "top right",
  }} >
      <h1 className="text-2xl font-bold mb-4">VTM Character Creator</h1>

      {/* BASIC INFO */}
      <input
        placeholder="Name"
        className={inputStyle}
        onChange={(e) => updateField("name", e.target.value)}
      />

      <input
        placeholder="Concept"
        className={inputStyle}
        onChange={(e) => updateField("concept", e.target.value)}
      />

      <select
        className="border p-2 w-full mb-4"
        onChange={(e) => updateField("predator", e.target.value)}
      >
        <option>Alleycat</option>
        <option>Bagger</option>
        <option>Blood Leech</option>
        <option>Cleaver</option>
        <option>Consensualist</option>
        <option>Sandman</option>
        <option>Farmer</option>
        <option>Grim Reaper</option>
        <option>Scene Queen</option>
      </select>

      <input
        placeholder="Sire"
        className={inputStyle}
        onChange={(e) => updateField("sire", e.target.value)}
      />

      <input
        placeholder="Generation"
        className={inputStyle}
        onChange={(e) => updateField("generation", e.target.value)}
      />

      <input
        placeholder="Ambition"
        className={inputStyle}
        onChange={(e) => updateField("ambition", e.target.value)}
      />

      <input
        placeholder="Desire"
        className={inputStyle}
        onChange={(e) => updateField("desire", e.target.value)}
      />

      <input
        placeholder="Clan"
        className={inputStyle}
        onChange={(e) => updateField("clan", e.target.value)}
      />

      <input
        placeholder="Age"
        className={inputStyle}
        onChange={(e) => updateField("age", e.target.value)}
      />

      {/* ATTRIBUTES */}
      <h2 className="text-xl mt-2 mb-2">Attributes</h2>

      <div className="parent-container gap-3">
        {Object.entries(character.attributes).map(([category, attrs]) => (
          <div key={category} className="sub-section border border-green-500 p-4 rounded-lg bg-black" >
            <h3 className="font-semibold text-center capitalize" >
              {category}
            </h3>

            <div className="position-modifier">
              {Object.entries(attrs).map(([attr, val]) => (
                <div key={attr} className="parent-container sub-section position-modifier">
                  <span>{attr}</span>
                  <input
                    type="number"
                    min="0"
                    max="5"
                    value={val}
                    onChange={(e) =>
                      updateNested("attributes", category, attr, parseInt(e.target.value))
                    }
                    className="text-center"
                  />
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
              

      {/* SKILLS */}
      <h2 className="text-xl mt-6 mb-2">Skills</h2>

      <div className="parent-container gap-6">
        {Object.entries(character.skills).map(([category, skills]) => (
          <div key={category} className="border border-green-500 p-4 rounded-lg bg-black">
            <h3 className="subsection font-semibold text-center mb-2 capitalize">
              {category}
            </h3>

            <div className="space-y-2">
              {Object.entries(skills).map(([skill, val]) => (
                <div key={skill} className="flex justify-between items-center">
                  <span className="border">{skill}</span>
                  <input
                    type="number"
                    min="0"
                    max="5"
                    value={val}
                    onChange={(e) =>
                      updateNested("skills", category, skill, parseInt(e.target.value))
                    }
                    className="border w-16 text-center"
                  />
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* DISCIPLINES */}
      <h2 className="text-xl mt-4">Disciplines</h2>

      <button
        className="bg-black border border-green-500 text-green-400 px-2 py-1 hover:bg-green-500 hover:text-black"
        onClick={() => updateDiscipline("new_discipline", 1)}
      >
        + Add Discipline
      </button>

      {Object.entries(character.disciplines).map(([name, val]) => (
        <div key={name} className="flex justify-between">
          <input
            value={name}
            onChange={(e) => {
              const newName = e.target.value;
              const updated = { ...character.disciplines };
              delete updated[name];
              updated[newName] = val;
              setCharacter({ ...character, disciplines: updated });
            }}
            className="border"
          />

          <input
            type="number"
            min="0"
            max="5"
            value={val}
            onChange={(e) =>
              updateDiscipline(name, parseInt(e.target.value))
            }
            className="border w-16"
          />
        </div>
      ))}

      {/* ADVANTAGE */}

      <h2 className="text-xl mt-4">Advantages</h2>

      <button
        className="bg-black border border-green-500 text-green-400 px-2 py-1 hover:bg-green-500 hover:text-black"
        onClick={() => updateAdvantage("new_discipline", "")}
      >
        + Add Advantage
      </button>

      {Object.entries(character.advantages).map(([name, val]) => (
        <div key={name} className="flex justify-between">
          <input
            value={name}
            onChange={(e) => {
              const newName = e.target.value;
              const updated = { ...character.advantages };
              delete updated[name];
              updated[newName] = val;
              setCharacter({ ...character, advantages: updated });
            }}
            className="border"
          />

          <input
            type="number"
            min="0"
            max="5"
            value={val}
            onChange={(e) =>
              updateAdvantage(name, parseInt(e.target.value))
            }
            className="border w-16"
          />
        </div>
        ))}

         {/* DISADVANTAGE */}

      <h2 className="text-xl mt-4">Disadvantages</h2>

      <button
        className="bg-black border border-green-500 text-green-400 px-2 py-1 hover:bg-green-500 hover:text-black"
        onClick={() => updateDisadvantage("new_disadvantage", "")}
      >
        + Add Advantage
      </button>

      {Object.entries(character.disadvantages).map(([name, val]) => (
        <div key={name} className="flex justify-between">
          <input
            value={name}
            onChange={(e) => {
              const newName = e.target.value;
              const updated = { ...character.disadvantages };
              delete updated[name];
              updated[newName] = val;
              setCharacter({ ...character, disadvantages: updated });
            }}
            className="border"
          />

          <input
            type="number"
            min="0"
            max="5"
            value={val}
            onChange={(e) =>
              updateDisadvantage(name, parseInt(e.target.value))
            }
            className="border w-16"
          />
        </div>
        ))}

        <button
          onClick={submitCharacter}
          className="mt-4 border border-green-500 px-4 py-2 hover:bg-green-500 hover:text-black"
        >
          Register Kindred
        </button>



      {/* OUTPUT */}
      <pre className="mt-6 bg-black border border-green-500 p-4 text-sm text-green-400">
        {JSON.stringify(character, null, 2)}
      </pre>
    </div>
  );
}