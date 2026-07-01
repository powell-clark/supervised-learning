# TASK-SL14: Lesson 9b: RNN practical — sequence modeling, time series forecasting, NumPy LSTM implementation

## Context

Create the practical notebook for Recurrent Neural Networks. Apply RNNs and LSTMs to sequence modeling and time series forecasting. Demonstrate from-scratch LSTM from theory and compare to PyTorch implementation.

## Acceptance Criteria

- [ ] Notebook file created: `notebooks/9d_rnn_practical.ipynb`
- [ ] Sequence modeling dataset: Real time series (stock prices, weather, or similar)
- [ ] Basic RNN implementation: Train vanilla RNN using PyTorch, show limitations
- [ ] LSTM implementation: Train LSTM, demonstrate improved gradient flow
- [ ] Time series preprocessing: Normalization, train/test split, sequence preparation
- [ ] From-scratch NumPy LSTM: Implement from 9c theory, show forward/backward pass
- [ ] Forecasting task: Predict future values from historical sequence
- [ ] Sequence-to-sequence: Demonstrate encoder-decoder architecture if applicable
- [ ] Hyperparameter selection: Hidden size, learning rate, sequence length effects
- [ ] Vanishing gradient empirical demonstration: Compare RNN vs LSTM gradient magnitudes
- [ ] Performance analysis: MAE, RMSE, visual predictions vs actuals
- [ ] Visualization: Predictions over time, hidden state evolution, gradient flow comparison
- [ ] No emojis, no corporate buzzwords
- [ ] References cited: PyTorch documentation, time series textbooks
- [ ] Notebook length: 70 hours effort

## Technical Notes

Time series setup: Create sliding windows of length T for input, predict T+1.

Vanishing gradients: RNN gradients decay; LSTM gradients remain stable (additive path through cell state).

## Definition of Done

- [ ] Notebook renders without errors
- [ ] All acceptance criteria verified
- [ ] NumPy LSTM matches PyTorch in results (within numerical precision)
- [ ] Vanishing gradient problem is empirically demonstrated
- [ ] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL13 (requires understanding from theory notebook)
