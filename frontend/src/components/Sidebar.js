import './Sidebar.css';

function Sidebar({ documents }) {
  return (
    <div className="sidebar">

      <div className="documents-title">Your documents</div>

      {documents.length === 0 ? (
        <div className="empty-documents">
          Upload something...
        </div>
      ) : (
        documents.map((doc, idx) => (
        <div key={idx} className="document-item">
          {doc}
        </div>
      )))}
    </div>
  );
}

export default Sidebar;