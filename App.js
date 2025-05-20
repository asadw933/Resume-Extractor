import React, { useState } from "react";
import axios from "axios";
import './App.css';

function App() {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("https://resume-extractor-jlfa.onrender.com", formData); // Change this in production
      setSkills(res.data.skills);
    } catch (err) {
      console.error("Upload error", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Resume Skill Extractor</h1>
      <input type="file" accept=".pdf,.txt" onChange={handleUpload} />
      {loading ? <p>Extracting...</p> : (
        <div className="skills">
          {skills.map((skill, i) => <span key={i} className="tag">{skill}</span>)}
        </div>
      )}
    </div>
  );
}

export default App;
const res = await axios.post("http://localhost:5000/upload", formData);
