import { useRef, useState } from 'react';
import { uploadFileAPI } from '../services/api';
import './Upload.css';

function Upload() {
  const fileInputRef = useRef(null);
  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState("");
  
  let timeoutId;
  const showMessage = (text, type) => {
    setMessage(text);
    setMessageType(type);

    clearTimeout(timeoutId);

    timeoutId = setTimeout(() => {
      setMessage("");
      setMessageType("");
    }, 5000);
  };

  const handleClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    try {
      await uploadFileAPI(file);
      showMessage("File uploaded", "success");
    } catch (err) {
      console.error(err);
      showMessage("Failed", "error");
    }
  };

  return (
    <div className="upload-container">
      <button className="upload-button" onClick={handleClick}>
        Upload file
      </button>

      <input
        type="file"
        accept=".pdf,.txt"
        ref={fileInputRef}
        onChange={handleFileChange}
        style={{ display: "none" }}
      />

      {message && (
        <div className={`upload-message ${messageType}`}>
          {message}
        </div>
      )}
    </div>
  );
}

export default Upload;