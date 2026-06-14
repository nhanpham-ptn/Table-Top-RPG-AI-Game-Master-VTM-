import './App.css';

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import CharacterCreator from "./Character";
import Start from "./Start"
import Loading from "./Loading"
import Gameplay from './Gameplay';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Start />} />
        <Route path="/character" element={<CharacterCreator />} />
        <Route path="/loading" element={<Loading />} />
        <Route path="/gameplay" element={<Gameplay />} />
      </Routes>
    </BrowserRouter>
  );
}



export default App;
