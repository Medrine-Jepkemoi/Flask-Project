import React, { useState } from 'react';
import axios from 'axios';
import './HomeCard.css'; 

const HomeCard = ({ home }) => {
  const [showReviewForm, setShowReviewForm] = useState(false);
  const [review, setReview] = useState('');

  const handlePurchase = () => {
    setShowReviewForm(true);
  };

  const handleSubmitReview = async (e) => {
    e.preventDefault();

    try {
      await axios.post('/api/reviews', { review, homeId: home.property_id });

      setReview('');
      setShowReviewForm(false);
    } catch (error) {
      console.log('Error submitting review:', error);
    }
  };

  return (
    <div className="home-card">
      <div className="home-card-inner">
        <div className="home-image">
          <img src={home.image} alt={home.title} />
          <div className="sticker">{home.sale ? 'On Sale' : 'For Rent'}</div>
        </div>
        <div className="home-details">
          <h2>{home.title}</h2>
          <p>Price: {home.price}</p>
          <p>{home.description}</p>
          <button onClick={handlePurchase}>Purchase</button>
        </div>
      </div>
      {showReviewForm && (
        <div className="review-form">
          <h3>Leave a Review</h3>
          <form onSubmit={handleSubmitReview}>
            <textarea
              value={review}
              onChange={(e) => setReview(e.target.value)}
              placeholder="Write your review"
              required
            ></textarea>
            <button type="submit">Submit</button>
          </form>
        </div>
      )}
    </div>
  );
};

export default HomeCard;
