import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [sentence, setSentence] = useState('');
  const [processedSentence, setProcessedSentence] = useState('');

  const handleMark = async () => {
    try {
      const response = await axios.post('http://localhost:8000/mark', { text: sentence });
      setProcessedSentence(response.data.marked_text);
    } catch (error) {
      console.error('Error in marking text:', error);
    }
  };

  const handleAnonymize = async () => {
    try {
      const response = await axios.post('http://localhost:8000/anonymize', { text: sentence });
      setProcessedSentence(response.data.anonymized_text);
    } catch (error) {
      console.error('Error in anonymizing text:', error);
    }
  };

  return (
      <div className="container">
        <section className="section ">
          <h1 className="eb-garamond-font has-text-weight-bold">Personal Information Filter</h1>
        </section>
        <section className="section">
          <div className="field">
            <div className="control">
            <textarea
                className="textarea"
                value={sentence}
                onChange={(e) => setSentence(e.target.value)}
                placeholder="Enter your sentence here"
            />
            </div>
          </div>
          <div className="field is-grouped">
            <div className="control">
              <button
                  className="button is-primary"
                  onClick={handleMark}
              >
                Mark Personal Information
              </button>
            </div>
            <div className="control">
              <button
                  className="button is-danger"
                  onClick={handleAnonymize}
              >
                Anonymize Information
              </button>
            </div>
          </div>
        </section>
        <section className="section">
          <div className="content">
            <h2 className="eb-garamond-font">Marked/Anonymized Text</h2>
            <div className="box" dangerouslySetInnerHTML={{ __html: processedSentence }} />
          </div>
        </section>
      </div>
  );
}

export default App;
