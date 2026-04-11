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