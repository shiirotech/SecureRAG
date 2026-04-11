export const askQuestionAPI = async (question) => {
  const response = await fetch(
    `http://127.0.0.1:8000/ask?question=${encodeURIComponent(question)}`,
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
    "http://127.0.0.1:8000/upload", {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error("Upload failed!");
  }

  return response.json();
}