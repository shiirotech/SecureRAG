import { useState, useEffect } from 'react';
import { askQuestionAPI, getDocumentsAPI } from '../services/api';
import Message from './Message';
import Upload from './Upload';
import Sidebar from './Sidebar';
import './Chat.css';

function Chat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [documents, setDocuments] = useState([]);

  const askQuestion = async () => {
    if (!question) return;

    const newMessages = [...messages, { role: "user", text: question}];
    setMessages(newMessages);
    setLoading(true);

    try {
      const data = await askQuestionAPI(question);
      setMessages([
        ...newMessages,
        {
          role: "assistant",
          text: data.answer,
          sources: data.sources,
        },
      ]);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
    setQuestion("");
  };

  const fetchDocuments = async () => {
    try {
      const data = await getDocumentsAPI();
      setDocuments(data.documents);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchDocuments();
  }, []);

  return (
    <div className="chat-layout">

      <Sidebar documents={documents} />

      <div className="chat-container">
        <div className="messages">
          {messages.map((msg, i) => (
            <Message key={i} msg={msg} />
          ))}

          {loading && <div>Thinking...</div>}
        </div>
          <div className="input-area">
            <div className="upload-section">
              <Upload onUploadSuccess={fetchDocuments} />
            </div>

            <input
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Type a question..."
            />

            <button onClick={askQuestion}>Ask</button>
          </div>
      </div>
    </div>
  );
}

export default Chat;