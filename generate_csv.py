# import pandas as pd

# # Manually reconstructing the cleaned table based on visual inspection of the image
# question_types = [
#     "Revisit Reasons Behind Preference Updates",
#     "Tracking Full Preference Evolution",
#     "Recall User Shared Facts",
#     "Acknowledge Latest User Preference",
#     "Provide Preference Aligned Recommendations",
#     "Generalize Reasons to New Scenarios",
#     "Suggest New Ideas"
# ]

# models = [
#     "Gemini 1.5-flash", "GPT-4.5", "Gemini 2.0-flash", "o1", "Gemini 2.0-flash-Lite",
#     "Deepseek RL-512B", "GPT-4o", "Llama3 4-Maverick", "GPT 4o-mini", "o3-mini",
#     "Claude 3.5-Haiku", "Claude 3.1-Haoss", "Claude 3.1-Sonnet", "Average", "Random Guess"
# ]

# data = [
#     [0.77, 0.76, 0.79, 0.75, 0.77, 0.83, 0.77, 0.76, 0.70, 0.72, 0.64, 0.41, 0.57, 0.71, 0.25],
#     [0.65, 0.68, 0.70, 0.67, 0.68, 0.68, 0.68, 0.66, 0.60, 0.54, 0.55, 0.38, 0.50, 0.61, 0.25],
#     [0.54, 0.61, 0.50, 0.52, 0.49, 0.43, 0.41, 0.37, 0.55, 0.47, 0.29, 0.30, 0.42, 0.44, 0.25],
#     [0.59, 0.55, 0.52, 0.54, 0.51, 0.42, 0.46, 0.43, 0.41, 0.39, 0.27, 0.31, 0.39, 0.42, 0.25],
#     [0.55, 0.44, 0.51, 0.42, 0.52, 0.49, 0.37, 0.42, 0.41, 0.32, 0.30, 0.27, 0.37, 0.40, 0.25],
#     [0.54, 0.46, 0.46, 0.39, 0.33, 0.38, 0.32, 0.32, 0.33, 0.30, 0.20, 0.27, 0.32, 0.35, 0.25],
#     [0.15, 0.27, 0.15, 0.25, 0.16, 0.16, 0.24, 0.20, 0.10, 0.11, 0.06, 0.20, 0.28, 0.18, 0.25]
# ]

# # Create a DataFrame
# results_qa_types = pd.DataFrame(data, columns=models, index=question_types)

# # Save to CSV
# csv_path = "static/csvs/results_qa_types.csv"
# results_qa_types.to_csv(csv_path)


