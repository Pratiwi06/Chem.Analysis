import streamlit as st

st.title("Chemical Analysis")
st.title("_chemical_ is :blue[cool] :sunglasses:")
import React, { useState } from "react";
import Slide1 from "./Slide1";
import Slide2 from "./Slide2";

function App() {
  const [tab, setTab] = useState("slide1");

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Slide App dengan Tabs</h1>
      <div className="flex space-x-4 mb-4">
        <button onClick={() => setTab("slide1")}>Slide 1</button>
        <button onClick={() => setTab("slide2")}>Slide 2</button>
      </div>
      <div className="border p-4 rounded">
        {tab === "slide1" && <Slide1 />}
        {tab === "slide2" && <Slide2 />}
      </div>
    </div>
  );
}

export default App;
