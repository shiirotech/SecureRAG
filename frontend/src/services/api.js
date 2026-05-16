const API_URL = "http://localhost:8000";

export const askQuestionAPI = async (question) => {
  const response = await fetch(
    `${API_URL}/ask?question=${encodeURIComponent(question)}`,
    {
      method: "POST",
    }
  );

  if (!response.ok) {
    throw new Error("API request failed!");
  }

  return response.json();
};

export const uploadFileAPI = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(
    `${API_URL}/upload`, {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error("Upload failed!");
  }

  return response.json();
};

export const getDocumentsAPI = async () => {
  const response = await fetch(`${API_URL}/documents`);

  if (!response.ok) {
    throw new Error("Failed to fetch documents!");
  }

  return response.json();
};