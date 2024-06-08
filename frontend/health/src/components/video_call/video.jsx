import React from 'react';
import { useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import './video.css';

const Homepage = () => {
    const [value, setValue] = useState();
    const navigate = useNavigate();
    const handleClick = useCallback(() => { 
        navigate(`/video/room/${value}`);
    }, [navigate, value]);    
  return (
    <div className='maincontainer'>
      <div className='container'>
        <input value={value} onChange={(e) => setValue(e.target.value)} type="text" placeholder='Enter room code' className='input-field'/>
        <br />
        <button onClick={handleClick} className='join'>Join</button>
        <a href="/" className="text-white pt-2"><button>Return Homepage</button></a>
      </div>
    </div>
  )
};

export default Homepage;