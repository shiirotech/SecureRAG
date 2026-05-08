import './Sidebar.css';

function Sidebar({ documents }) {
  return (
    <div className="sidebar">

      <h2>Documents</h2>

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