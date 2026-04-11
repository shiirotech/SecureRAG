import { useState } from 'react';
import { askQuestionAPI } from '../services/api';
import Message from './Message';
import './Chat.css';

function Chat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

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

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, i) => (
          <Message key={i} msg={msg} />
        ))}

        {loading && <div>Thinking...</div>}
      </div>

      <div className="input-area">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask a question..."
        />
        <button onClick={askQuestion}>Ask</button>
      </div>
    </div>
  );
}

export default Chat;