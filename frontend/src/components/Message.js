import './Message.css';
import ReactMarkdown from 'react-markdown';

function Message({ msg }) {
  return (
    <div className={`message-row ${msg.role}`}>
      <div className="message">
        <div className="message-text">
          <b>{msg.role}:</b>
          <ReactMarkdown>
            {msg.text}
          </ReactMarkdown>
        </div>

        {msg.sources && (
          <div className="sources">
            <b>Sources:</b>
            {msg.sources.map((s, idx) => (
              <div key={idx}>
                {s.document} (page {s.page})
              </div>
            ))}
          </div>
        )}
      </div>
    </div>  
  );
}

export default Message;