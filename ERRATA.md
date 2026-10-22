# Errata and open findings

These findings come from an independent academic review on 2026-10-22, and the author works through them as he studies the lessons.

Review identifiers identify shared findings repeated under each affected file; cell numbers are the review’s original zero-based numbers, and Markdown documents retain their original line references.

## [0a_linear_regression_theory.ipynb](notebooks/0a_linear_regression_theory.ipynb)

- [fixed] P1 — cell 22 — P1-01: Convexity does not establish uniqueness. — Require full column rank for uniqueness and a positive step size below twice the reciprocal largest Hessian eigenvalue for gradient-descent convergence.

- [fixed] P1 — cell 21 — P1-02: The bootstrap quantity is not squared bias. — Label the quantity as squared deviation from the observed response and state that it includes observation noise.

- [open] P2 — cell 11, 22 — P2-01: Scaling invariance is stated in the wrong coordinates. — Distinguish prediction equivalence, coefficient transformation, and conditioning.

- [open] P2 — cell 18 — P2-25: “No setup” omits the data-location prerequisite. — Include a Colab bootstrap/download step and document the working directory and required files.

## [0b_linear_regression_practical.ipynb](notebooks/0b_linear_regression_practical.ipynb)

- [fixed] P1 — cell 5, 16–18 — P1-03: The regularization equations do not match the library parameterization. — Present each estimator’s actual objective, distinguish `alpha` from `l1_ratio`, and state the intercept convention.

- [open] P1 — cell 13, 15, 17 — P1-04: Target encoding leaks labels across the internal CV folds. — Refit preprocessing within every tuning fold and cross-fit supervised encodings for training rows.

- [open] P1 — cell 29 — P1-05: High cardinality is confused with the dummy-variable trap. — Distinguish rank deficiency, dimensionality, sparsity, and statistical efficiency; explain dropping a reference category and regularized alternatives.

- [open] P2 — cell 7 — P2-25: “No setup” omits the data-location prerequisite. — Include a Colab bootstrap/download step and document the working directory and required files.

- [open] P3 — cell 25 — P3-02: Internal task-management commentary remains in teaching material. — Retain the substantive limitation or methodological explanation and remove internal workflow references.

## [1a_logistic_regression_theory.ipynb](notebooks/1a_logistic_regression_theory.ipynb)

- [fixed] P1 — cell 31–36 — P1-06: Cancer labels are reversed, corrupting the clinical interpretations. — Preserve 0 = malignant and 1 = benign, explicitly use class 0 for cancer metrics, and correct the counts and malignancy probabilities.

- [open] P1 — cell 17, 19, 32 — P1-07: Standardization is presented as creating normality, separation, and true importance. — Explain optimization conditioning and coefficient units, and remove normality and “true importance” claims.

- [open] P1 — cell 20 — P1-08: The initialization variance calculations are wrong. — Use the appropriate uniform bound \(\sqrt{6/(n_{\rm in}+n_{\rm out})}\), state the assumptions, and remove the claimed guaranteed Gaussian percentages.

- [open] P1 — cell 22, 24 — P1-09: The loss-function comparison teaches incorrect gradients and growth rates. — Derive each derivative with respect to the logit and weights, and describe \(-\log p_y\) accurately.

- [open] P2 — cell 37–38 — P2-02: The learning-rate comparison confounds initialization and optimization. — Use common initial weights, repeat across seeds, show convergence diagnostics, and choose the rate without consulting test performance.

## [1b_logistic_regression_practical.ipynb](notebooks/1b_logistic_regression_practical.ipynb)

- [fixed] P1 — cell 6, 10, 21 — P1-06: Cancer labels are reversed, corrupting the clinical interpretations. — Preserve 0 = malignant and 1 = benign, explicitly use class 0 for cancer metrics, and correct the counts and malignancy probabilities.

- [open] P1 — cell 11 — P1-07: Standardization is presented as creating normality, separation, and true importance. — Explain optimization conditioning and coefficient units, and remove normality and “true importance” claims.

- [open] P1 — cell 11 — P1-08: The initialization variance calculations are wrong. — Use the appropriate uniform bound \(\sqrt{6/(n_{\rm in}+n_{\rm out})}\), state the assumptions, and remove the claimed guaranteed Gaussian percentages.

- [open] P1 — cell 11 — P1-10: The displayed full-batch update omits the features. — Use \(X^\top(\hat p-y)/m\) for weights and the mean residual for the bias.

- [open] P1 — cell 11 — P1-11: Training mode is confused with gradient tracking. — Distinguish module mode from `requires_grad`, `no_grad`, and inference mode.

- [open] P1 — cell 11 — P1-12: Adam’s denominator is misstated. — Put epsilon outside the square root and reconcile the contradictory formula in cell 12.

- [open] P1 — cell 10 — P1-13: The “best” checkpoints continue changing during training. — Deep-copy the state or clone every tensor when improvement occurs.

- [open] P1 — cell 13 — P1-14: Test data are used to select configurations and thresholds. — Make every choice on validation data or nested CV, then evaluate once on an untouched test set.

- [open] P1 — cell 19 — P1-16: ROC-AUC is interpreted as probability quality. — Describe discrimination and separately assess probabilities using reliability plots and proper scoring rules.

- [open] P1 — cell 14 — P1-17: The clinical-deployment conclusion is unsupported. — Remove the deployment conclusion and limit the claim to this educational classification experiment; explain the missing external validation and clinically relevant error analysis.

- [open] P2 — cell 14 — P2-03: GPU runtime claims lack a corresponding reproducible execution path. — Provide the exact device-enabled benchmark, environment, repetitions, and measured outputs, or remove the timings.

## [2a_decision_trees_theory.ipynb](notebooks/2a_decision_trees_theory.ipynb)

- [open] P1 — cell 31 — P1-18: Entropy fails on zero-count classes. — Skip zero counts and define behaviour for an empty input.

- [open] P1 — cell 42 — P1-19: The decision-tree bias–variance explanation gives the wrong decomposition. — State the assumptions and full decomposition; show validation error potentially falling before rising.

- [open] P1 — cell 46 — P1-20: Impurity importance is missing required weighting or normalization. — Include \(n_{\rm node}/N\), sum contributions, then explicitly normalize if describing normalized importance.

## [2b_decision_trees_practical.ipynb](notebooks/2b_decision_trees_practical.ipynb)

- [open] P1 — cell 28–31 — P1-21: Training target encodings include the row’s own target despite the stated guarantee. — Cross-fit every supervised training feature, including hierarchical priors, while fitting inference mappings on the complete training partition.

- [open] P1 — cell 38–40 — P1-22: MAE changes units between explanation and implementation. — Label log-MAE and pound-MAE separately and state exactly which metric drives selection.

- [open] P1 — cell 40 — P1-23: A boxplot of configuration scores is interpreted as property-level residual analysis. — Interpret the point as a configuration-level score; use held-out residuals grouped by property type to investigate the proposed explanation.

- [open] P1 — cell 45 — P1-26: The random-forest variance formula assumes away tree correlation. — Under equal variance and common correlation, use \(\sigma^2[\rho+(1-\rho)/M]\), explaining the assumptions.

- [open] P1 — cell 61 — P1-27: Encoding choices are assigned unsupported market and temporal properties. — Distinguish target-derived inputs, supervised training targets, chronological modelling, and empirically tested robustness.

- [open] P1 — cell 62 — P1-28: The validation strategy is described as something the code does not implement. — Describe the actual random-split evaluation, or implement appropriate grouped and chronological splits.

- [open] P1 — cell 55–56 — P1-29: KL divergence is treated as a percentage and is not the implemented statistic. — Choose and define each statistic, implement that definition, and calibrate thresholds without translating KL values into percentages.

- [open] P1 — cell 56–58 — P1-30: The historical monitoring simulation records events at the current time. — Pass event timestamps and an evaluation clock explicitly, and start each experiment with isolated state.

- [open] P1 — cell 56 — P1-31: Missing monitoring baselines silently produce zero measured change. — Initialize reference statistics from training/reference data and return “baseline unavailable” when absent; do not report missing evidence as market stability.

- [open] P1 — cell 52 — P1-34: The combined encoder’s construction and serialization contracts disagree. — Implement a consistent object round trip or an explicit versioned state dictionary, and initialize all components needed by `fit()`.

- [open] P2 — cell 50–51 — P2-04: Tree disagreement is treated as validated uncertainty. — Call it tree disagreement, measure its relationship with held-out errors, and distinguish it from intervals with demonstrated coverage.

- [open] P2 — cell 56 — P2-05: Monitoring does not handle its advertised optional ground truth. — Distinguish pending labels from invalid inputs and compute supervised metrics only on labelled rows.

## [2c_decision_trees_ATLAS_model_comparison.ipynb](notebooks/2c_decision_trees_ATLAS_model_comparison.ipynb)

- [open] P1 — cell 10 — P1-21: Training target encodings include the row’s own target despite the stated guarantee. — Cross-fit every supervised training feature, including hierarchical priors, while fitting inference mappings on the complete training partition.

- [open] P1 — cell 13–14 — P1-22: MAE changes units between explanation and implementation. — Label log-MAE and pound-MAE separately and state exactly which metric drives selection.

- [open] P1 — cell 1, 14, 17 — P1-24: Explained log-price variation is reported as explained price variation. — Say “log-price variance” or compute and report a separate price-scale \(R^2\).

- [open] P1 — cell 13 — P1-25: Predicting the training mean does not guarantee test \(R^2=0\). — Distinguish the evaluation-mean reference in the definition from a deployable training-mean baseline.

- [open] P1 — cell 17 — P1-27: Encoding choices are assigned unsupported market and temporal properties. — Distinguish target-derived inputs, supervised training targets, chronological modelling, and empirically tested robustness.

- [open] P1 — cell 14, 17 — P1-28: The validation strategy is described as something the code does not implement. — Describe the actual random-split evaluation, or implement appropriate grouped and chronological splits.

- [open] P1 — cell 10 — P1-32: Production features do not reproduce the training feature schema. — Persist the chosen feature-set specification, column names, order, and transformations together with the fitted model.

- [open] P1 — cell 10 — P1-33: The unseen-postcode fallback produces NaNs. — Fill missing counts with zero before computing weights, and verify that the result equals the parent encoding.

- [open] P2 — cell 15–16 — P2-27: Cross-validation standard deviations are called confidence intervals. — Label them as fold variability or justify a specific interval construction and its limitations.

- [open] P3 — cell 13 — P3-02: Internal task-management commentary remains in teaching material. — Retain the substantive limitation or methodological explanation and remove internal workflow references.

## [3a_neural_networks_theory.ipynb](notebooks/3a_neural_networks_theory.ipynb)

- [open] P1 — cell 13 — P1-35: The general output-layer derivative incorrectly assumes independent activations. — Give the general Jacobian-transpose rule, then derive the softmax–cross-entropy cancellation separately.

- [open] P2 — cell 18 — P2-06: The scratch loss and analytical gradient are not exactly the same objective. — Calculate binary loss from logits with `logaddexp`, and multiclass loss with log-sum-exp, matching their derivatives.

- [open] P2 — cell 15 — P2-07: Random initialization is presented as a mathematical necessity. — Explain the particular symmetry and state the recommendation without a universal necessity claim.

## [3b_neural_networks_practical.ipynb](notebooks/3b_neural_networks_practical.ipynb)

- [open] P1 — cell 12, 20 — P1-13: The “best” checkpoints continue changing during training. — Deep-copy the state or clone every tensor when improvement occurs.

- [open] P1 — cell 26, 28 — P1-14: Test data are used to select configurations and thresholds. — Make every choice on validation data or nested CV, then evaluate once on an untouched test set.

- [open] P1 — cell 35 — P1-36: Similar accuracies are presented as evidence of equivalent optimization. — Document these differences and avoid interpreting predictive agreement as implementation or optimization verification.

- [open] P1 — cell 40 — P1-37: Percent differences are calculated on centered standardized features. — Report differences in standard-deviation units or transform measurements back to their original units before discussing percentages.

## [4a_svm_theory.ipynb](notebooks/4a_svm_theory.ipynb)

- [open] P1 — cell 27 — P1-38: The kernel “SVM” does not optimize the SVM dual. — Implement a valid constrained dual optimizer, such as paired SMO updates, or rename and derive the algorithm actually implemented.

- [open] P1 — cell 25 — P1-39: The linear SVM update is not the gradient of its reported loss. — Make the objective, gradient normalization, and meaning of \(C\) consistent.

- [open] P1 — cell 33 — P1-40: The margin interpretation points toward the wrong fitting failure. — Explain the regularization trade-off without treating weight norm alone as a universal diagnostic.

- [open] P1 — cell 22 — P1-41: The soft-margin limit lacks the separability condition. — State the separable case separately.

- [open] P1 — cell 17 — P1-42: The sigmoid expression is presented as an unrestricted valid kernel. — Explain that the expression is not a universally valid Mercer kernel and state any domain or parameter restrictions being assumed.

- [open] P1 — cell 35 — P1-43: Preprocessing is fitted before held-out evaluation splits. — Split first and fit preprocessing only on training data; during CV, place preprocessing inside the fold-fitted pipeline.

## [4b_support_vector_machines_practical.ipynb](notebooks/4b_support_vector_machines_practical.ipynb)

- [open] P2 — cell 19–20 — P2-08: The promised scratch-versus-library SVM comparison is absent. — Run both implementations under a shared evaluation protocol after fixing the scratch solver, or rename the section.

## [5a_k_nearest_neighbors_theory.ipynb](notebooks/5a_k_nearest_neighbors_theory.ipynb)

- [open] P1 — cell 33, 42 — P1-43: Preprocessing is fitted before held-out evaluation splits. — Split first and fit preprocessing only on training data; during CV, place preprocessing inside the fold-fitted pipeline.

- [open] P1 — cell 8, 26, 40 — P1-44: Distance concentration is reversed when taking reciprocals. — Use a consistent fixed-sample-size concentration statement and distinguish absolute distance growth from relative distance contrast.

- [open] P1 — cell 40 — P1-45: The hypersphere-volume formula is wrong. — Use \(V_d(r)=\pi^{d/2}r^d/\Gamma(d/2+1)\), specifying the radius when comparing with a cube; reconcile this appendix with the different formula earlier in the notebook.

- [open] P1 — cell 40–41 — P1-46: The fixed-1NN risk bound is misrepresented as consistency at the optimal risk. — State the binary fixed-1NN asymptotic bound \(2R^*(1-R^*)\) separately from consistency with suitable \(k_n\to\infty\), \(k_n/n\to0\).

- [open] P1 — cell 39–40 — P1-47: A finite-sample complexity formula is asserted without the assumptions it needs. — Remove the theorem-like claim or provide a precise theorem with its assumptions and source.

- [open] P1 — cell 28 — P1-48: General \(k\)-NN does not have zero training error. — Restrict the interpolation claim to the appropriate 1NN setting.

- [open] P1 — cell 11, 16, 24, 31, 39 — P1-49: Complexity claims do not describe the supplied implementations. — Derive costs for the actual code, including dimension, selection method, and balance assumptions.

- [open] P1 — cell 20, 39–40 — P1-50: Voronoi geometry is confused with classification geometry. — Distinguish sites, cells, faces, and class regions.

- [open] P1 — cell 40 — P1-51: Non-norms and sensitivity to large coordinates are misstated. — Require \(p\ge1\) for norms and describe \(0<p<1\) as a quasi-norm setting.

- [open] P1 — cell 41 — P1-52: Cosine distance is conflated with angular distance and a metric. — Distinguish cosine similarity, cosine dissimilarity, angular distance, and Euclidean distance between normalized vectors.

- [open] P1 — cell 40 — P1-53: Whitening uses the wrong matrix power. — Derive Mahalanobis distance as \(\|\Sigma^{-1/2}(x-\mu)\|_2\).

- [open] P1 — cell 43 — P1-54: The LSH implementation neither supplies independent hash tables nor returns nearest neighbours. — Implement an actual randomized hash family and distance reranking, or label this as an incomplete candidate-bucketing illustration.

- [open] P2 — cell 14 — P2-09: The \(k\)-NN variance identity omits conditioning. — State the conditioning explicitly and use total variance when discussing randomness over complete training datasets.

- [open] P2 — cell 24 — P2-10: Dimension thresholds are taught as universal rules. — Label such cutoffs as rough computational heuristics and demonstrate dependence on the data-generating setting.

- [open] P2 — cell 42 — P2-11: Reported numerical results lack a reproducible experiment. — Supply the experiment or explicitly label every number as hypothetical.

- [open] P2 — cell 22, 38 — P2-12: Vendor deployment assertions are uncited. — Cite technical publications for each assertion or replace named deployments with clearly hypothetical applications.

- [open] P3 — cell 23–24, 30, 36, 38–43 — P3-03: Repeated conclusions obscure the authoritative account. — Consolidate into one conclusion and a narrowly scoped appendix after resolving the substantive contradictions above.

## [5b_knn_practical.ipynb](notebooks/5b_knn_practical.ipynb)

- [fixed] P1 — cell 43–44 — P1-06: Cancer labels are reversed, corrupting the clinical interpretations. — Preserve 0 = malignant and 1 = benign, explicitly use class 0 for cancer metrics, and correct the counts and malignancy probabilities.

- [open] P1 — cell 44 — P1-43: Preprocessing is fitted before held-out evaluation splits. — Split first and fit preprocessing only on training data; during CV, place preprocessing inside the fold-fitted pipeline.

- [open] P1 — cell 8 — P1-55: The custom KNN metric parameter is ignored. — Dispatch to implemented metric functions and reject unsupported names, or remove the parameter.

- [open] P1 — cell 38 — P1-56: The anomaly threshold is fitted on a different statistic from the prediction statistic. — Use the same score definition in calibration and prediction, explicitly excluding self-neighbours during calibration.

- [open] P2 — cell 26 — P2-28: An arbitrary distance transformation is labelled confidence. — Call it a distance-based heuristic, or calibrate an explicitly defined confidence estimate on separate validation data.

## [6a_naive_bayes_theory.ipynb](notebooks/6a_naive_bayes_theory.ipynb)

- [open] P1 — cell 34 — P1-57: Pairwise conditional independence is substituted for the Naive Bayes assumption. — State mutual conditional independence and qualify the Gaussian covariance illustration.

- [open] P2 — cell 8 — P2-13: Joint-distribution complexity is overgeneralized. — Identify the model family before discussing parameter counts.

- [open] P2 — cell 36 — P2-14: A confidence histogram does not assess calibration. — Plot a reliability diagram and report a proper probability score; do not infer overconfidence from a histogram alone.

## [6b_naive_bayes_practical.ipynb](notebooks/6b_naive_bayes_practical.ipynb)

- [open] P1 — cell 1 — P1-58: Sparse documents are confused with the zero-frequency problem. — Distinguish document sparsity from class-conditional unseen events.

- [open] P1 — cell 7, 10 — P1-59: The IDF explanation disagrees with both arithmetic and code. — Present \(\log((N+1)/(\mathrm{df}+1))+1\) for that implementation and explain each smoothing term.

- [open] P2 — cell 24 — P2-15: Frequent class words are called informative words. — Either rename the plot or use a discriminative contrast such as smoothed class log-odds.

## [7a_ensemble_methods_theory.ipynb](notebooks/7a_ensemble_methods_theory.ipynb)

- [open] P1 — cell 9 — P1-20: Impurity importance is missing required weighting or normalization. — Include \(n_{\rm node}/N\), sum contributions, then explicitly normalize if describing normalized importance.

- [open] P1 — cell 12 — P1-60: Better-than-chance rounds do not alone imply exponential decay in round count. — Introduce a uniform weak-learning edge \(\mathrm{err}_m\le1/2-\gamma\), or retain the bound involving the sum of squared round-specific edges.

- [open] P2 — cell 10 — P2-16: The forest-correlation demonstration estimates a different quantity from the variance formula. — Distinguish those quantities and use repeated training datasets or resampling to estimate the latter.

## [7b_ensemble_methods_practical.ipynb](notebooks/7b_ensemble_methods_practical.ipynb)

- [open] P1 — cell 10–11 — P1-15: The ensemble lesson explicitly trains its stopping rule on the test set. — Create a separate early-stopping validation partition and reserve the test partition for final evaluation.

- [open] P1 — cell 18 — P1-61: The supposedly matched boosting comparison does not match row sampling. — Enable LightGBM bagging explicitly and explain that matching parameter names does not establish equivalent algorithms or capacity.

- [open] P1 — cell 25 — P1-62: A comparison between different algorithms is called a regularization ablation. — Vary regularization within one otherwise controlled implementation.

## [8a_anomaly_detection_theory.ipynb](notebooks/8a_anomaly_detection_theory.ipynb)

- [open] P1 — cell 7–8, 26 — P1-53: Whitening uses the wrong matrix power. — Derive Mahalanobis distance as \(\|\Sigma^{-1/2}(x-\mu)\|_2\).

- [open] P1 — cell 13 — P1-63: The LOF intuition reverses the density comparison. — Describe a locally sparse point adjacent to denser neighbours, consistently with the formula immediately below.

## [8b_anomaly_detection_practical.ipynb](notebooks/8b_anomaly_detection_practical.ipynb)

- [open] P1 — cell 18, 20 — P1-14: Test data are used to select configurations and thresholds. — Make every choice on validation data or nested CV, then evaluate once on an untouched test set.

- [open] P1 — cell 7, 12, 24 — P1-64: Label-dependent training is described as label-free fitting. — Describe semi-supervised novelty detection with a known-normal reference set, or train the unsupervised comparison on the unfiltered training population.

- [open] P1 — cell 17 — P1-65: The ROC/PR dominance claim contradicts the relevant theorem. — Distinguish pointwise curve dominance from AUC ordering.

- [open] P2 — cell 15 — P2-17: ROC-AUC’s probabilistic interpretation omits ties. — Include ties, particularly because tree-derived and other discrete scores can contain many of them.

## [9a_cnn_theory.ipynb](notebooks/9a_cnn_theory.ipynb)

- [open] P1 — cell 30 — P1-66: An identity skip does not guarantee an undiminished total gradient. — Describe the direct identity path and its optimization benefit without claiming a universal lower bound on the resulting gradient.

- [open] P2 — cell 26 — P2-06: The scratch loss and analytical gradient are not exactly the same objective. — Calculate binary loss from logits with `logaddexp`, and multiclass loss with log-sum-exp, matching their derivatives.

- [open] P2 — cell 14 — P2-18: Batch normalization is given an overstrong representational argument. — Qualify the moment normalization and distinguish fixed-statistics inference from batch-dependent training.

## [9b_cnn_practical.ipynb](notebooks/9b_cnn_practical.ipynb)

- [open] P1 — cell 15 — P1-67: The “frozen” ResNet backbone still updates batch-normalization state. — Keep the frozen backbone’s batch-normalization modules in evaluation mode while training the head, or explicitly teach the intended adaptation of those buffers.

- [open] P1 — cell 22, 24 — P1-68: The NumPy/PyTorch timing comparison measures different work. — Time equivalent regions, control initialization and numerical precision where relevant, and synchronize any asynchronous accelerator work.

- [open] P2 — cell 21 — P2-06: The scratch loss and analytical gradient are not exactly the same objective. — Calculate binary loss from logits with `logaddexp`, and multiclass loss with log-sum-exp, matching their derivatives.

## [9c_rnn_theory.ipynb](notebooks/9c_rnn_theory.ipynb)

- [open] P1 — cell 7 — P1-69: The BPTT derivation mixes row and column conventions. — Use \(dh_t=W_{hy}^\top\delta_t+W_{hh}^\top dz_{t+1}\), or rewrite all equations consistently as row-vector equations.

- [open] P1 — cell 10–11, 29 — P1-70: Spectral radius, spectral norm, and gradient-growth guarantees are conflated. — State sufficient norm bounds carefully and distinguish upper bounds, transient amplification, and observed products.

- [open] P1 — cell 13 — P1-71: The direct LSTM memory path is presented as the complete derivative. — Label it as one gradient path and explain the additional Jacobian terms.

- [open] P1 — cell 9, 31 — P1-72: One training demonstration is called a proof that a vanilla RNN cannot learn the task. — Report failure under the stated experimental settings and distinguish optimization difficulty from representational impossibility.

- [open] P1 — cell 14 — P1-73: The claimed floating-point underflow contradicts the saved evidence. — Use matched sequence lengths and report the actual values, distinguishing small gradients from numerical underflow.

- [open] P2 — cell 15, 25, 27 — P2-19: GRU parameter counts do not match the supplied bias convention. — Count the actual parameter arrays and identify the chosen GRU variant and bias convention.

## [9d_rnn_practical.ipynb](notebooks/9d_rnn_practical.ipynb)

- [open] P1 — cell 25 — P1-74: Bidirectional encoders are incorrectly ruled out for forecasting. — Distinguish bidirectional processing of past inputs from access to future targets.

- [open] P2 — cell 32 — P2-20: Forecasting scores combine different prediction tasks. — Compare matching origins and horizons, report error by horizon, and include a seasonal-naive baseline.

## [9e_transformer_theory.ipynb](notebooks/9e_transformer_theory.ipynb)

- [open] P1 — cell 16 — P1-75: The decoder silently ignores its attention output projections. — Apply the output projections before the residual additions or explicitly derive a different simplified architecture.

- [open] P2 — cell 9 — P2-21: Positional-encoding extrapolation is confused with model generalization. — Distinguish encoding availability from empirical length generalization and state the frequencies or wavelengths correctly.

- [open] P2 — cell 15–16 — P2-22: Decoder causality needs an explicit shifted-target prerequisite. — Introduce the start token and right-shifted target sequence before explaining why the mask makes teacher forcing causal.

## [9f_transformer_practical.ipynb](notebooks/9f_transformer_practical.ipynb)

- [open] P1 — cell 14, 20 — P1-76: BLEU is incorrectly rejected because the task has one deterministic correct answer. — Explain that BLEU permits a single reference, while exact-match accuracy fits this task because it requires exact correctness rather than partial n-gram credit.

- [open] P2 — cell 16 — P2-23: DistilBERT pretraining omits its defining distillation objective. — Explain the teacher–student objective and distinguish it from simply training a smaller MLM.

- [open] P3 — cell 0 — P3-01: The lesson identifier is wrong. — Change the identifier to 9F.

- [open] P3 — cell 0 — P3-02: Internal task-management commentary remains in teaching material. — Retain the substantive limitation or methodological explanation and remove internal workflow references.

## [CURRICULUM_ROADMAP.md](CURRICULUM_ROADMAP.md)

- [open] P2 — cell n/a (lines 3–9, 24–85 in the review) — P2-24: The roadmap describes an obsolete repository as current. — Update the inventory and status descriptions, or explicitly identify the document as an archived plan.

- [open] P2 — cell n/a (lines 12–14, 138–146 in the review) — P2-26: Symbol and byte counts are used as academic quality criteria. — Replace them with explicit learning outcomes, derivation obligations, assumptions, numerical checks, and evaluation requirements.

## [README.md](README.md)

- [open] P2 — cell n/a (line 6 in the review) — P2-25: “No setup” omits the data-location prerequisite. — Include a Colab bootstrap/download step and document the working directory and required files.

## Counts

Unique review findings (shared findings counted once):

| Grade | Open | Fixed |
|---|---:|---:|
| P1 | 72 | 4 |
| P2 | 28 | 0 |
| P3 | 3 | 0 |

Entries above (shared findings counted under every affected file):

| Grade | Open | Fixed |
|---|---:|---:|
| P1 | 85 | 6 |
| P2 | 32 | 0 |
| P3 | 5 | 0 |
