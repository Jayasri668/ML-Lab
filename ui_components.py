"""
Modern, Professional UI Components, Visualizations, and Style System for Streamlit App
Provides rich medical-tech aesthetic, interactive steppers, diagnostic cards, and responsive layout.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st


def set_custom_style():
    """Injects custom CSS styling for a modern medical-tech workstation UI."""
    custom_css = """
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main App Header */
    .hero-header {
        background: linear-gradient(135deg, #090d16 0%, #111e33 45%, #0d5f57 100%);
        padding: 28px 36px;
        border-radius: 20px;
        color: #ffffff;
        margin-bottom: 20px;
        box-shadow: 0 14px 36px -8px rgba(13, 95, 87, 0.35);
        border: 1px solid rgba(255, 255, 255, 0.12);
        position: relative;
        overflow: hidden;
    }
    .hero-header::after {
        content: "";
        position: absolute;
        top: -60%;
        right: -10%;
        width: 340px;
        height: 340px;
        background: radial-gradient(circle, rgba(45, 212, 191, 0.3) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(20, 184, 166, 0.18);
        color: #2dd4bf;
        padding: 5px 14px;
        border-radius: 24px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 12px;
        border: 1px solid rgba(45, 212, 191, 0.35);
        backdrop-filter: blur(8px);
    }
    .hero-header h1 {
        color: #ffffff !important;
        font-size: 2.15rem;
        font-weight: 800;
        letter-spacing: -0.035em;
        margin: 0 0 8px 0;
        line-height: 1.2;
    }
    .hero-header p {
        color: #94a3b8 !important;
        font-size: 1.05rem;
        font-weight: 400;
        margin: 0;
        max-width: 850px;
    }

    /* Interactive Pipeline Progress Stepper */
    .pipeline-stepper-container {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 22px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    }
    .stepper-title {
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #64748b;
        margin-bottom: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .stepper-track {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
    }
    .step-item {
        background: #f8fafc;
        border: 1.5px solid #e2e8f0;
        border-radius: 12px;
        padding: 10px 14px;
        display: flex;
        align-items: center;
        gap: 10px;
        transition: all 0.2s ease;
    }
    .step-item.active {
        background: #f0fdfa;
        border-color: #0d9488;
        box-shadow: 0 4px 12px rgba(13, 148, 136, 0.12);
    }
    .step-item.complete {
        background: #f0fdf4;
        border-color: #10b981;
    }
    .step-num {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 0.8rem;
        background: #e2e8f0;
        color: #475569;
        flex-shrink: 0;
    }
    .step-item.active .step-num {
        background: #0d9488;
        color: #ffffff;
    }
    .step-item.complete .step-num {
        background: #10b981;
        color: #ffffff;
    }
    .step-info-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #0f172a;
        line-height: 1.2;
    }
    .step-info-sub {
        font-size: 0.74rem;
        color: #64748b;
        margin-top: 2px;
    }

    /* Notice Banner */
    .disclaimer-banner {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
        border-left: 4px solid #f59e0b;
        padding: 12px 18px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: #92400e;
        font-size: 0.88rem;
        line-height: 1.45;
        font-weight: 500;
        box-shadow: 0 2px 6px rgba(245, 158, 11, 0.08);
        border-top: 1px solid #fde68a;
        border-right: 1px solid #fde68a;
        border-bottom: 1px solid #fde68a;
    }

    /* Quick Action Card */
    .quick-action-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        border-radius: 16px;
        padding: 22px 26px;
        margin-bottom: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.15);
    }
    .quick-action-box h4 {
        color: #38bdf8 !important;
        margin: 0 0 6px 0;
        font-size: 1.15rem;
    }
    .quick-action-box p {
        color: #cbd5e1 !important;
        font-size: 0.92rem;
        margin-bottom: 14px;
    }

    /* Modern Metric Cards */
    .metric-card-pro {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        position: relative;
    }
    .metric-card-pro:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 24px rgba(15, 118, 110, 0.09);
        border-color: #cbd5e1;
    }
    .metric-card-pro .tag {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: #64748b;
        margin-bottom: 6px;
    }
    .metric-card-pro .val {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0f172a;
        font-family: 'Plus Jakarta Sans', sans-serif;
        line-height: 1.1;
    }
    .metric-card-pro .desc {
        font-size: 0.8rem;
        color: #0d9488;
        font-weight: 600;
        margin-top: 6px;
    }

    /* Diagnostic Result Cards with Dynamic Severity */
    .result-card-normal {
        background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
        border: 2px solid #10b981;
        border-radius: 18px;
        padding: 28px 32px;
        margin: 20px 0;
        box-shadow: 0 12px 32px rgba(16, 185, 129, 0.12);
    }
    .result-card-fatty {
        background: linear-gradient(135deg, #fffbeb 0%, #ffffff 100%);
        border: 2px solid #f59e0b;
        border-radius: 18px;
        padding: 28px 32px;
        margin: 20px 0;
        box-shadow: 0 12px 32px rgba(245, 158, 11, 0.12);
    }
    .result-card-cirrhosis {
        background: linear-gradient(135deg, #fef2f2 0%, #ffffff 100%);
        border: 2px solid #ef4444;
        border-radius: 18px;
        padding: 28px 32px;
        margin: 20px 0;
        box-shadow: 0 12px 32px rgba(239, 68, 68, 0.12);
    }
    .result-card-default {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
        border: 2px solid #0d9488;
        border-radius: 18px;
        padding: 28px 32px;
        margin: 20px 0;
        box-shadow: 0 12px 32px rgba(13, 148, 136, 0.12);
    }

    .badge-normal {
        background: #dcfce7;
        color: #15803d;
        padding: 5px 14px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }
    .badge-fatty {
        background: #fef3c7;
        color: #b45309;
        padding: 5px 14px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }
    .badge-cirrhosis {
        background: #fee2e2;
        color: #b91c1c;
        padding: 5px 14px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }
    .badge-default {
        background: #ccfbf1;
        color: #0f766e;
        padding: 5px 14px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 12px;
    }

    .result-class-name {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 16px;
        text-transform: uppercase;
        letter-spacing: -0.02em;
    }
    .result-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #f1f5f9;
        font-size: 0.95rem;
    }
    .result-row:last-child {
        border-bottom: none;
    }
    .result-row-lbl {
        color: #64748b;
        font-weight: 600;
    }
    .result-row-val {
        color: #0f172a;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
    }
    .result-clinical-disclaimer {
        margin-top: 18px;
        padding: 12px 16px;
        background: #f8fafc;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        color: #475569;
        font-size: 0.85rem;
        line-height: 1.5;
    }

    /* Step Pill */
    .step-pill {
        display: inline-block;
        background: #e0f2fe;
        color: #0284c7;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }

    /* Pipeline Status Indicators */
    .status-badge-ready {
        display: inline-block;
        background: #dcfce7;
        color: #15803d;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
    }
    .status-badge-pending {
        display: inline-block;
        background: #f1f5f9;
        color: #64748b;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Sample Card Box */
    .sample-preset-card {
        background: #ffffff;
        border: 1.5px solid #e2e8f0;
        border-radius: 14px;
        padding: 14px;
        text-align: center;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    .sample-preset-card:hover {
        border-color: #0d9488;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(13, 148, 136, 0.12);
    }
    .sample-preset-card h5 {
        margin: 8px 0 4px 0;
        font-size: 0.95rem;
        font-weight: 700;
        color: #0f172a;
    }
    .sample-preset-card p {
        font-size: 0.78rem;
        color: #64748b;
        margin: 0 0 10px 0;
        line-height: 1.35;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def render_header():
    """Renders the main application title and subtitle."""
    st.markdown(
        """
        <div class="hero-header">
            <div class="hero-badge">🩺 ACADEMIC & RESEARCH WORKSTATION</div>
            <h1>LIVER ULTRASOUND IMAGE CLASSIFICATION</h1>
            <p>Interactive Machine Learning & Traditional Computer Vision Pipeline (HOG + GLCM + Multi-Classifier)</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_pipeline_stepper(dataset_ready: bool, features_ready: bool, model_ready: bool, model_name: str = None, total_images: int = 0):
    """Renders an interactive 4-step pipeline status tracker at the top of the workstation."""
    step1_cls = "complete" if dataset_ready else "active"
    step2_cls = "complete" if features_ready else ("active" if dataset_ready else "")
    step3_cls = "complete" if model_ready else ("active" if features_ready else "")
    step4_cls = "complete" if model_ready else ""

    s1_sub = f"{total_images} Images Loaded" if dataset_ready else "Load or Scan Dataset"
    s2_sub = "HOG + GLCM Vector Ready" if features_ready else "Awaiting Feature Extraction"
    s3_sub = f"{model_name}" if model_ready else "Select & Train Classifier"
    s4_sub = "Live Prediction Available" if model_ready else "Requires Trained Model"

    s1_icon = "✓" if dataset_ready else "1"
    s2_icon = "✓" if features_ready else "2"
    s3_icon = "✓" if model_ready else "3"
    s4_icon = "✓" if model_ready else "4"

    stepper_html = f"""
    <div class="pipeline-stepper-container">
        <div class="stepper-title">
            <span>⚙️ ML PIPELINE PROGRESS TRACKER</span>
            <span>{"🟢 SYSTEM READY FOR CLASSIFICATION" if model_ready else "🟡 PIPELINE IN PROGRESS"}</span>
        </div>
        <div class="stepper-track">
            <div class="step-item {step1_cls}">
                <div class="step-num">{s1_icon}</div>
                <div>
                    <div class="step-info-title">1. Dataset</div>
                    <div class="step-info-sub">{s1_sub}</div>
                </div>
            </div>
            <div class="step-item {step2_cls}">
                <div class="step-num">{s2_icon}</div>
                <div>
                    <div class="step-info-title">2. Features</div>
                    <div class="step-info-sub">{s2_sub}</div>
                </div>
            </div>
            <div class="step-item {step3_cls}">
                <div class="step-num">{s3_icon}</div>
                <div>
                    <div class="step-info-title">3. Model</div>
                    <div class="step-info-sub">{s3_sub}</div>
                </div>
            </div>
            <div class="step-item {step4_cls}">
                <div class="step-num">{s4_icon}</div>
                <div>
                    <div class="step-info-title">4. Inference</div>
                    <div class="step-info-sub">{s4_sub}</div>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(stepper_html, unsafe_allow_html=True)


def render_disclaimer():
    """Renders the mandatory educational/academic disclaimer."""
    st.markdown(
        """
        <div class="disclaimer-banner">
            <strong>⚠️ Educational Notice:</strong> This application is developed for academic demonstration, mini-project presentation, and research benchmarking. It is not a medical device and should not be used for clinical diagnosis.
        </div>
        """,
        unsafe_allow_html=True
    )


def render_metric_cards(accuracy: float, precision: float, recall: float, f1: float):
    """Renders modern 4-metric score cards with clean styling."""
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card-pro">
                <div class="tag">Accuracy Score</div>
                <div class="val">{accuracy * 100:.2f}%</div>
                <div class="desc">Overall Correctness</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card-pro">
                <div class="tag">Precision (Weighted)</div>
                <div class="val">{precision * 100:.2f}%</div>
                <div class="desc">Positive Predictive Value</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card-pro">
                <div class="tag">Recall (Weighted)</div>
                <div class="val">{recall * 100:.2f}%</div>
                <div class="desc">Sensitivity Rate</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card-pro">
                <div class="tag">F1-Score</div>
                <div class="val">{f1 * 100:.2f}%</div>
                <div class="desc">Harmonic Mean</div>
            </div>
            """,
            unsafe_allow_html=True
        )


def plot_confusion_matrix(cm: np.ndarray, class_names: list):
    """
    Renders an enhanced Seaborn confusion matrix heatmap with percentage and count annotations.
    """
    fig, ax = plt.subplots(figsize=(6.5, 5))
    
    with np.errstate(divide='ignore', invalid='ignore'):
        cm_pct = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
        cm_pct = np.nan_to_num(cm_pct)

    annot_matrix = np.empty_like(cm, dtype=object)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            annot_matrix[i, j] = f"{cm[i, j]}\n({cm_pct[i, j]:.1f}%)"

    sns.heatmap(
        cm,
        annot=annot_matrix,
        fmt="",
        cmap="Blues",
        xticklabels=class_names,
        yticklabels=class_names,
        cbar=True,
        linewidths=1.2,
        linecolor="#f1f5f9",
        ax=ax,
        annot_kws={"size": 11, "weight": "bold", "color": "#0f172a"}
    )
    ax.set_title("Liver Ultrasound Confusion Matrix", fontsize=12, weight="bold", pad=15)
    ax.set_xlabel("Predicted Class", fontsize=10, weight="bold", labelpad=10)
    ax.set_ylabel("Actual Ground Truth", fontsize=10, weight="bold", labelpad=10)
    plt.tight_layout()
    return fig


def plot_class_distribution(class_counts: dict):
    """
    Plots a polished horizontal bar chart of dataset classes.
    """
    fig, ax = plt.subplots(figsize=(7, max(3, len(class_counts) * 0.75)))
    classes = list(class_counts.keys())
    counts = list(class_counts.values())

    palette = sns.color_palette("mako", len(classes))
    bars = ax.barh(classes, counts, color=palette, height=0.55, edgecolor="#94a3b8", alpha=0.9)

    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + max(max(counts) * 0.02, 0.5),
            bar.get_y() + bar.get_height() / 2,
            f"{int(width)} images",
            va="center",
            ha="left",
            fontsize=9.5,
            weight="bold",
            color="#1e293b"
        )

    ax.set_xlabel("Number of Images", fontsize=9.5, weight="bold")
    ax.set_ylabel("Class Subfolder", fontsize=9.5, weight="bold")
    ax.set_title("Dataset Class Distribution", fontsize=11.5, weight="bold", pad=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    return fig


def plot_glcm_radar(glcm_summary: dict):
    """
    Plots a radar (spider) chart for normalized GLCM texture properties.
    """
    properties = ["contrast", "dissimilarity", "homogeneity", "energy", "correlation"]
    labels = [p.capitalize() for p in properties]

    raw_values = [glcm_summary[p]["mean"] for p in properties]
    norm_values = []
    for val in raw_values:
        norm_values.append(min(1.0, max(0.05, abs(val) if abs(val) <= 1.0 else np.log10(abs(val) + 1.0) / 2.0)))

    values = norm_values + [norm_values[0]]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += [angles[0]]

    fig, ax = plt.subplots(figsize=(4.8, 4.8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color="#0d9488", alpha=0.35)
    ax.plot(angles, values, color="#0d9488", linewidth=2.2, marker="o", markersize=6)

    ax.set_thetagrids(np.degrees(angles[:-1]), labels, fontsize=9, weight="bold")
    ax.set_ylim(0, 1.0)
    ax.set_title("GLCM Second-Order Texture Profile", fontsize=11, weight="bold", pad=15)
    plt.tight_layout()
    return fig


def plot_roc_curves(roc_data: dict):
    """
    Plots Multi-Class One-vs-Rest ROC Curves.
    """
    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    
    colors = sns.color_palette("Set2", len(roc_data))
    for (cls_name, data), color in zip(roc_data.items(), colors):
        fpr = data["fpr"]
        tpr = data["tpr"]
        roc_auc = data["auc"]
        ax.plot(
            fpr, tpr,
            label=f"{cls_name} (AUC = {roc_auc:.3f})",
            color=color,
            lw=2.2
        )

    ax.plot([0, 1], [0, 1], "k--", lw=1.2, label="Random Guess (AUC = 0.50)")
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel("False Positive Rate (1 - Specificity)", fontsize=9.5, weight="bold")
    ax.set_ylabel("True Positive Rate (Sensitivity)", fontsize=9.5, weight="bold")
    ax.set_title("Receiver Operating Characteristic (ROC) Curves", fontsize=11.5, weight="bold", pad=12)
    ax.legend(loc="lower right", fontsize=8.5, frameon=True)
    ax.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    return fig


def plot_model_comparison_chart(comparison_df: pd.DataFrame):
    """
    Plots a multi-metric comparison bar chart for all algorithms.
    """
    df_melted = comparison_df.melt(
        id_vars=["Algorithm"],
        value_vars=["Accuracy", "Precision", "Recall", "F1 Score"],
        var_name="Metric",
        value_name="Score"
    )

    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    sns.barplot(
        data=df_melted,
        x="Metric",
        y="Score",
        hue="Algorithm",
        palette="mako",
        ax=ax,
        edgecolor="#cbd5e1"
    )

    ax.set_ylim(0.0, 1.12)
    ax.set_ylabel("Metric Score (0.0 - 1.0)", fontsize=9.5, weight="bold")
    ax.set_xlabel("Evaluation Metric", fontsize=9.5, weight="bold")
    ax.set_title("Machine Learning Models Performance Comparison", fontsize=11.5, weight="bold", pad=12)
    ax.legend(title="Algorithm", frameon=True, fontsize=8.5)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    for p in ax.patches:
        height = p.get_height()
        if not np.isnan(height) and height > 0:
            ax.annotate(
                f"{height:.2f}",
                (p.get_x() + p.get_width() / 2.0, height),
                ha="center",
                va="bottom",
                fontsize=8,
                weight="bold",
                xytext=(0, 2),
                textcoords="offset points"
            )

    plt.tight_layout()
    return fig


def render_prediction_result(
    predicted_class: str,
    algorithm: str,
    confidence: float = None,
    probabilities: dict = None,
    feature_summary: dict = None
):
    """
    Renders the standardized prediction result card with dynamic severity styling and acoustic explanation.
    """
    conf_str = f"{confidence * 100:.2f}%" if confidence is not None else "N/A (Decision Boundary Model)"

    p_lower = predicted_class.lower()
    if "normal" in p_lower:
        card_class = "result-card-normal"
        badge_class = "badge-normal"
        severity_label = "🟢 NORMAL / HEALTHY HEPATIC PARENCHYMA"
        clinical_note = "Acoustic texture shows homogeneous echogenicity with normal acoustic speckle and clear vascular structures."
    elif "fatty" in p_lower:
        card_class = "result-card-fatty"
        badge_class = "badge-fatty"
        severity_label = "🟡 FATTY LIVER / STEATOSIS DETECTED"
        clinical_note = "Acoustic texture exhibits diffuse parenchymal hyperechogenicity ('bright liver') with posterior sound attenuation."
    elif "cirrhosis" in p_lower or "fibrosis" in p_lower:
        card_class = "result-card-cirrhosis"
        badge_class = "badge-cirrhosis"
        severity_label = "🔴 CIRRHOSIS / ADVANCED FIBROSIS DETECTED"
        clinical_note = "Acoustic texture shows coarse heterogeneous nodularity with irregular hyperechoic fibrotic reticular acoustic bands."
    else:
        card_class = "result-card-default"
        badge_class = "badge-default"
        severity_label = f"🔵 CLASSIFIED: {predicted_class.upper()}"
        clinical_note = "Pattern classified according to acoustic feature representations in the dataset."

    st.markdown(
        f"""
        <div class="{card_class}">
            <div class="{badge_class}">{severity_label}</div>
            <div class="result-class-name">Classification: {predicted_class}</div>
            
            <div class="result-row">
                <span class="result-row-lbl">🤖 Classifier Model:</span>
                <span class="result-row-val">{algorithm}</span>
            </div>
            <div class="result-row">
                <span class="result-row-lbl">🔍 Feature Representation:</span>
                <span class="result-row-val">HOG Gradients + GLCM Texture (Multi-Angular)</span>
            </div>
            <div class="result-row">
                <span class="result-row-lbl">🎯 Confidence Score:</span>
                <span class="result-row-val">{conf_str}</span>
            </div>
            
            <div class="result-clinical-disclaimer">
                <strong>🔬 Acoustic Texture Insight:</strong> {clinical_note}<br>
                <small style="color:#64748b; margin-top:4px; display:block;">⚠️ <em>For educational and academic presentation purposes only. Not a medical diagnosis.</em></small>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if probabilities and len(probabilities) > 1:
        st.markdown("#### 📊 Multi-Class Probability Breakdown")
        prob_cols = st.columns(len(probabilities))
        for i, (cls_name, prob) in enumerate(probabilities.items()):
            with prob_cols[i % len(prob_cols)]:
                st.metric(
                    label=f"Class: {cls_name}",
                    value=f"{prob * 100:.1f}%"
                )
                st.progress(float(prob))


def generate_diagnostic_text_report(
    predicted_class: str,
    algorithm: str,
    confidence: float,
    probabilities: dict,
    image_name: str
) -> str:
    """Generates a downloadable markdown/text academic report for the classification result."""
    from datetime import datetime
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conf_str = f"{confidence * 100:.2f}%" if confidence is not None else "N/A"
    
    prob_lines = ""
    if probabilities:
        prob_lines = "\n".join([f"- **{k}**: {v*100:.2f}%" for k, v in probabilities.items()])
    else:
        prob_lines = "- Not available for this model type"

    report = f"""# 🩺 Liver Ultrasound Image Classification Report
**Generated by:** Liver Ultrasound ML Classifier System  
**Timestamp:** {now_str}  
**Input Image Reference:** `{image_name}`  

---

## 📌 Executive Diagnostic Summary
- **Predicted Class:** **{predicted_class}**
- **Classification Model:** {algorithm}
- **Confidence Level:** {conf_str}

## 📊 Class Probability Breakdown
{prob_lines}

## 🔬 Feature Extraction Methodology
1. **Grayscale Conversion & Standardization:** Resized to 128x128 pixels.
2. **Noise Reduction:** Gaussian Blur spatial filtering for ultrasound speckle suppression.
3. **Contrast Enhancement:** Histogram Equalization / CLAHE to accentuate parenchymal textures.
4. **HOG (Histogram of Oriented Gradients):** 9 Orientations, 8x8 pixels per cell, 2x2 cells per block.
5. **GLCM (Gray-Level Co-occurrence Matrix):** Contrast, Dissimilarity, Homogeneity, Energy, Correlation across 4 angles (0°, 45°, 90°, 135°).

---
*Notice: This report was generated by an academic machine learning research workstation and is intended strictly for educational evaluation and project demonstration.*
"""
    return report
