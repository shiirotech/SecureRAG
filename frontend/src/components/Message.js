import './Message.css';

function Message({ msg }) {
  return (
    <div className={`message-row ${msg.role}`}>
      <div className="message">
        <div className="message-text">
          <b>{msg.role}:</b> {msg.text}
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