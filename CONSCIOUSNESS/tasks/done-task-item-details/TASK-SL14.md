# TASK-SL14: Lesson 9b: RNN practical — sequence modeling, time series forecasting, NumPy LSTM implementation

## Context

Create the practical notebook for Recurrent Neural Networks. Apply RNNs and LSTMs to sequence modeling and time series forecasting. Demonstrate from-scratch LSTM from theory and compare to PyTorch implementation.

## Acceptance Criteria

- [x] Notebook file created: `notebooks/9d_rnn_practical.ipynb`
- [x] Sequence modeling dataset: Real time series (stock prices, weather, or similar) — Box & Jenkins airline passengers (1949-1960, monthly, real, trend+seasonality)
- [x] Basic RNN implementation: Train vanilla RNN using PyTorch, show limitations — explicit-equation PyTorch RNN cell, autograd-trained; limitations shown via the window-length sweep (train MSE degrades 2.9x→4.5x vs LSTM as window grows 6→24 months)
- [x] LSTM implementation: Train LSTM, demonstrate improved gradient flow — explicit-equation PyTorch LSTM; gradient-magnitude measurement (cell 24) shows LSTM retaining more gradient at longer T from an identical starting point
- [x] Time series preprocessing: Normalization, train/test split, sequence preparation — chronological split (last 24 months held out, never shuffled), train-only normalization statistics, sliding windows
- [x] From-scratch NumPy LSTM: Implement from 9c theory, show forward/backward pass — reused 9C's `LSTMCell` verbatim, trained on this task with its own BPTT (test MAE=68.35, RMSE=78.85)
- [x] Forecasting task: Predict future values from historical sequence — one-month-ahead forecast from a 12-month window
- [x] Sequence-to-sequence: Demonstrate encoder-decoder architecture if applicable — 6-month-ahead free-running encoder-decoder (test MAE=62.11, RMSE=68.93)
- [x] Hyperparameter selection: Hidden size, learning rate, sequence length effects — window length (6/12/24), hidden size (8/32), learning rate (0.005/0.02) all swept with real trained results
- [x] Vanishing gradient empirical demonstration: Compare RNN vs LSTM gradient magnitudes — same fixed-weight model measured at T=6/12/24/48; LSTM retains 4.1x more gradient than RNN by T=48
- [x] Performance analysis: MAE, RMSE, visual predictions vs actuals — comparison table across all 4 models plus predictions-vs-actuals plot
- [x] Visualization: Predictions over time, hidden state evolution, gradient flow comparison — all three produced (cells 26, 28, 24 respectively)
- [x] No emojis, no corporate buzzwords — scanned programmatically, none found
- [x] References cited: PyTorch documentation, time series textbooks — PyTorch docs, Hyndman & Athanasopoulos "Forecasting: Principles and Practice", Box & Jenkins (the series' origin), Sutskever et al. 2014 (seq2seq), plus back-reference to 9C
- [x] Notebook length: 70 hours effort — effort is inherently unverifiable as a criterion; matches the depth of the sibling 9b_cnn_practical.ipynb (30 cells, comparable LaTeX density, real dataset, from-scratch/PyTorch/comparison structure)

## Technical Notes

Time series setup: Create sliding windows of length T for input, predict T+1.

Vanishing gradients: RNN gradients decay; LSTM gradients remain stable (additive path through cell state).

## Definition of Done

- [x] Notebook renders without errors — `jupyter nbconvert --to notebook --execute`, 0 error outputs across 30 cells
- [x] All acceptance criteria verified
- [x] NumPy LSTM matches PyTorch in results (within numerical precision) — weight-copied equivalence check, max abs difference 2.8e-17 on identical input
- [x] Vanishing gradient problem is empirically demonstrated — both via the window-length training-loss gap and the direct fixed-weight gradient-magnitude measurement
- [x] Ready for peer review and publication

## Story Points

14 (70 hours estimated effort)

## Blocked By

TASK-SL13 (requires understanding from theory notebook)
