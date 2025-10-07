"""
Simple Linear Regression with CRISP-DM Methodology
===================================================

This application demonstrates the complete CRISP-DM process for a simple linear regression problem.
Users can adjust parameters and see real-time results.

Author: AIoT HW1 Project
Date: 2025-10-07
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set page configuration
st.set_page_config(
    page_title="Linear Regression with CRISP-DM",
    page_icon="📊",
    layout="wide"
)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)


def generate_data(a, b, noise, n_points, random_state=42):
    """
    Generate synthetic data following the equation: y = a*x + b + noise
    
    Parameters:
    -----------
    a : float
        Slope of the line
    b : float
        Intercept of the line
    noise : float
        Standard deviation of Gaussian noise
    n_points : int
        Number of data points to generate
    random_state : int
        Random seed for reproducibility
        
    Returns:
    --------
    X : numpy array
        Feature values
    y : numpy array
        Target values
    """
    np.random.seed(random_state)
    X = np.linspace(-10, 10, n_points)
    y_true = a * X + b
    y = y_true + np.random.normal(0, noise, n_points)
    return X.reshape(-1, 1), y, y_true


def train_model(X_train, y_train):
    """
    Train a linear regression model
    
    Parameters:
    -----------
    X_train : numpy array
        Training features
    y_train : numpy array
        Training targets
        
    Returns:
    --------
    model : LinearRegression
        Trained model
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance
    
    Parameters:
    -----------
    model : LinearRegression
        Trained model
    X_test : numpy array
        Test features
    y_test : numpy array
        Test targets
        
    Returns:
    --------
    metrics : dict
        Dictionary containing MSE and R² scores
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    return {
        'mse': mse,
        'r2': r2,
        'predictions': y_pred
    }


def plot_regression(X, y, y_true, model, true_a, true_b):
    """
    Plot the regression line with data points
    
    Parameters:
    -----------
    X : numpy array
        Feature values
    y : numpy array
        Target values (with noise)
    y_true : numpy array
        True target values (without noise)
    model : LinearRegression
        Trained model
    true_a : float
        True slope
    true_b : float
        True intercept
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot data points
    ax.scatter(X, y, alpha=0.5, label='Data points', color='blue', s=30)
    
    # Plot true line
    ax.plot(X, y_true, 'g--', linewidth=2, label=f'True line (y = {true_a:.2f}x + {true_b:.2f})')
    
    # Plot predicted line
    y_pred = model.predict(X)
    learned_a = model.coef_[0]
    learned_b = model.intercept_
    ax.plot(X, y_pred, 'r-', linewidth=2, 
            label=f'Predicted line (y = {learned_a:.2f}x + {learned_b:.2f})')
    
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Linear Regression: Data Points and Fitted Line', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_predictions_vs_actual(y_test, y_pred):
    """
    Plot predicted values vs actual values
    
    Parameters:
    -----------
    y_test : numpy array
        Actual test values
    y_pred : numpy array
        Predicted values
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    
    ax.scatter(y_test, y_pred, alpha=0.5, color='purple', s=50)
    
    # Plot diagonal line (perfect prediction)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect prediction')
    
    ax.set_xlabel('Actual Values', fontsize=12)
    ax.set_ylabel('Predicted Values', fontsize=12)
    ax.set_title('Predicted vs Actual Values', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_residuals(X_test, y_test, y_pred):
    """
    Plot residuals
    
    Parameters:
    -----------
    X_test : numpy array
        Test features
    y_test : numpy array
        Actual test values
    y_pred : numpy array
        Predicted values
    """
    residuals = y_test - y_pred
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.scatter(X_test, residuals, alpha=0.5, color='orange', s=50)
    ax.axhline(y=0, color='r', linestyle='--', linewidth=2)
    
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Residuals', fontsize=12)
    ax.set_title('Residual Plot', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    return fig


def main():
    """
    Main Streamlit application
    """
    # Title and description
    st.title("📊 Simple Linear Regression with CRISP-DM")
    st.markdown("""
    This application demonstrates the complete **CRISP-DM (Cross-Industry Standard Process for Data Mining)** 
    methodology applied to a simple linear regression problem.
    
    Adjust the parameters in the sidebar to see how they affect the model's performance.
    """)
    
    # Sidebar for parameters
    st.sidebar.header("🎛️ Model Parameters")
    st.sidebar.markdown("Adjust these parameters to control the data generation and model behavior:")
    
    # Parameter inputs
    true_a = st.sidebar.slider(
        "Slope (a) in y = ax + b",
        min_value=-10.0,
        max_value=10.0,
        value=2.0,
        step=0.1,
        help="Controls the steepness of the line"
    )
    
    true_b = st.sidebar.slider(
        "Intercept (b) in y = ax + b",
        min_value=-10.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
        help="Controls where the line crosses the y-axis"
    )
    
    noise = st.sidebar.slider(
        "Noise Level (σ)",
        min_value=0.0,
        max_value=5.0,
        value=1.0,
        step=0.1,
        help="Standard deviation of Gaussian noise added to data"
    )
    
    n_points = st.sidebar.slider(
        "Number of Data Points",
        min_value=50,
        max_value=500,
        value=100,
        step=10,
        help="Total number of data points to generate"
    )
    
    test_size = st.sidebar.slider(
        "Test Set Size (%)",
        min_value=10,
        max_value=40,
        value=20,
        step=5,
        help="Percentage of data used for testing"
    ) / 100
    
    # CRISP-DM Process
    st.header("🔄 CRISP-DM Process")
    
    # Create tabs for each CRISP-DM phase
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "1️⃣ Business Understanding",
        "2️⃣ Data Understanding",
        "3️⃣ Data Preparation",
        "4️⃣ Modeling",
        "5️⃣ Evaluation",
        "6️⃣ Deployment"
    ])
    
    with tab1:
        st.subheader("Business Understanding")
        st.markdown("""
        **Objective**: Build a linear regression model to understand the relationship between variables.
        
        **Goals**:
        - Demonstrate how linear regression works
        - Show the impact of noise on model performance
        - Provide interactive learning experience
        
        **Success Criteria**:
        - Model accurately fits the linear relationship
        - Users can experiment with different parameters
        - Clear visualizations and metrics are provided
        """)
    
    with tab2:
        st.subheader("Data Understanding")
        
        # Generate data
        X, y, y_true = generate_data(true_a, true_b, noise, n_points)
        
        st.markdown(f"""
        **Data Generation**:
        - Formula: `y = {true_a:.2f} × x + {true_b:.2f} + noise`
        - Noise: Gaussian with σ = {noise:.2f}
        - Number of points: {n_points}
        """)
        
        # Display data statistics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("X Range", f"[{X.min():.2f}, {X.max():.2f}]")
            st.metric("X Mean", f"{X.mean():.2f}")
        with col2:
            st.metric("y Range", f"[{y.min():.2f}, {y.max():.2f}]")
            st.metric("y Mean", f"{y.mean():.2f}")
        
        # Show sample data
        df_sample = pd.DataFrame({'X': X.flatten()[:10], 'y': y[:10]})
        st.markdown("**Sample Data (first 10 points)**:")
        st.dataframe(df_sample, use_container_width=True)
    
    with tab3:
        st.subheader("Data Preparation")
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        st.markdown(f"""
        **Train/Test Split**:
        - Training set: {len(X_train)} samples ({(1-test_size)*100:.0f}%)
        - Test set: {len(X_test)} samples ({test_size*100:.0f}%)
        - Random state: 42 (for reproducibility)
        
        **Data Characteristics**:
        - No missing values (synthetic data)
        - No feature scaling needed (single feature)
        - Data is already in numerical format
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Training Samples", len(X_train))
        with col2:
            st.metric("Test Samples", len(X_test))
    
    with tab4:
        st.subheader("Modeling")
        
        # Train model
        model = train_model(X_train, y_train)
        
        st.markdown("""
        **Model Selection**: Linear Regression (Ordinary Least Squares)
        
        **Why Linear Regression?**
        - The underlying relationship is linear
        - Simple and interpretable
        - No hyperparameters to tune
        - Fast training and prediction
        """)
        
        # Display learned parameters
        learned_a = model.coef_[0]
        learned_b = model.intercept_
        
        st.markdown("**Learned Parameters**:")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Learned Slope (a)", f"{learned_a:.4f}", 
                     delta=f"{learned_a - true_a:.4f} from true")
        with col2:
            st.metric("Learned Intercept (b)", f"{learned_b:.4f}",
                     delta=f"{learned_b - true_b:.4f} from true")
        
        st.info(f"**Learned Equation**: y = {learned_a:.4f}x + {learned_b:.4f}")
        st.success(f"**True Equation**: y = {true_a:.2f}x + {true_b:.2f}")
    
    with tab5:
        st.subheader("Evaluation")
        
        # Evaluate model
        metrics = evaluate_model(model, X_test, y_test)
        
        st.markdown("**Performance Metrics on Test Set**:")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Mean Squared Error (MSE)", f"{metrics['mse']:.4f}")
            st.caption("Lower is better. Measures average squared error.")
        with col2:
            st.metric("R² Score", f"{metrics['r2']:.4f}")
            st.caption("Higher is better (max 1.0). Proportion of variance explained.")
        
        # Interpretation
        if metrics['r2'] > 0.9:
            st.success("✅ Excellent fit! The model explains >90% of the variance.")
        elif metrics['r2'] > 0.7:
            st.info("✓ Good fit. The model explains >70% of the variance.")
        elif metrics['r2'] > 0.5:
            st.warning("⚠️ Moderate fit. Consider investigating the data or model.")
        else:
            st.error("❌ Poor fit. The model struggles to explain the data.")
        
        # Visualizations
        st.markdown("---")
        st.markdown("### 📈 Visualizations")
        
        # Plot 1: Regression line
        st.markdown("#### 1. Regression Line with Data Points")
        fig1 = plot_regression(X, y, y_true, model, true_a, true_b)
        st.pyplot(fig1)
        plt.close()
        
        # Plot 2: Predictions vs Actual
        st.markdown("#### 2. Predicted vs Actual Values")
        fig2 = plot_predictions_vs_actual(y_test, metrics['predictions'])
        st.pyplot(fig2)
        plt.close()
        
        st.caption("Points closer to the red dashed line indicate better predictions.")
        
        # Plot 3: Residuals
        st.markdown("#### 3. Residual Analysis")
        fig3 = plot_residuals(X_test, y_test, metrics['predictions'])
        st.pyplot(fig3)
        plt.close()
        
        st.caption("Residuals should be randomly scattered around zero with no clear pattern.")
    
    with tab6:
        st.subheader("Deployment")
        
        st.markdown("""
        **Deployment Strategy**: This application is deployed using Streamlit Cloud.
        
        **Features**:
        - ✅ Interactive web interface
        - ✅ Real-time parameter adjustment
        - ✅ Automatic model retraining
        - ✅ Comprehensive visualizations
        - ✅ Educational CRISP-DM walkthrough
        
        **Usage**:
        1. Adjust parameters in the sidebar
        2. Observe how changes affect the model
        3. Analyze performance metrics and visualizations
        4. Experiment with different noise levels and sample sizes
        
        **Learning Points**:
        - Higher noise → Lower R², Higher MSE
        - More data points → More stable estimates
        - Linear regression finds best-fit line using least squares
        """)
        
        st.markdown("---")
        st.markdown("### 🚀 Deployment Information")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Local Deployment**:
            ```bash
            pip install -r requirements.txt
            streamlit run app.py
            ```
            """)
        with col2:
            st.markdown("""
            **Cloud Deployment**:
            - Platform: Streamlit Cloud
            - Repository: GitHub
            - Auto-updates on commit
            """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>📚 AIoT HW1 Project | Simple Linear Regression with CRISP-DM Methodology</p>
        <p>Built with ❤️ using Streamlit, Scikit-learn, and Python</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
