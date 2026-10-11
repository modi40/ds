import os
import sys
import glob
import py_compile

REQUIRED_FILES = [
    "apriori_association_rules.py",
    "apriori_groceries.py",
    "apriori_student_activities.py",
    "bar_chart_courses.py",
    "bar_chart_departments.py",
    "box_plot_outliers.py",
    "box_plot_sales_outliers.py",
    "correlation_heatmap.py",
    "correlation_heatmap_weather.py",
    "data_cleaning_iqr.py",
    "data_discretization_equal_frequency.py",
    "data_discretization_equal_width.py",
    "data_discretization_equal_width_books.py",
    "data_integration.py",
    "data_transformation_scaling.py",
    "dendrogram_products.py",
    "geospatial_treemap_world_cities.py",
    "geospatial_visualization.py",
    "histogram_titanic.py",
    "kmeans_clustering.py",
    "kmeans_clustering_ecommerce.py",
    "kmeans_clustering_students.py",
    "knn_customers.py",
    "knn_spam.py",
    "knn_student_grading.py",
    "knn_wine.py",
    "label_encoding.py",
    "linear_regression_crop_yield.py",
    "linear_regression_salary.py",
    "linear_regression_sports.py",
    "linear_regression_youtube.py",
    "logistic_regression_gaming.py",
    "logistic_regression_smartphones.py",
    "min_max_scaling.py",
    "normalization.py",
    "one_hot_encoding.py",
    "pca_feature_extraction.py",
    "pie_chart_payment_methods.py",
    "pie_chart_transportation.py",
    "polynomial_regression_car_prices.py",
    "polynomial_regression_songs.py",
    "random_forest_heart_disease.py",
    "random_forest_house_prices.py",
    "random_forest_student_grading.py",
    "scatter_plot_cars.py",
    "standardization.py",
    "treemap_3d_scatter_economy.py",
    "treemap_cities.py",
    "venn_diagram_streaming.py",
    "word_cloud_books.py"
]

def verify_all():
    base_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
    print("=" * 80)
    print("CS-308 Data Science Practicals: System & Code Verification")
    print(f"Working Directory: {base_dir}")
    print("=" * 80)

    all_passed = True
    missing_files = []
    empty_files = []
    syntax_errors = []
    missing_question_comments = []

    print(f"Checking {len(REQUIRED_FILES)} required Python practical programs...")
    for idx, fname in enumerate(REQUIRED_FILES, 1):
        fpath = os.path.join(base_dir, fname)
        if not os.path.exists(fpath):
            missing_files.append(fname)
            all_passed = False
            continue
        
        size = os.path.getsize(fpath)
        if size == 0:
            empty_files.append(fname)
            all_passed = False
            continue

        try:
            py_compile.compile(fpath, doraise=True)
        except Exception as e:
            syntax_errors.append((fname, str(e)))
            all_passed = False

        with open(fpath, "r", encoding="utf-8") as f:
            first_few = f.read(300)
            if not ("QUESTION:" in first_few and "#" in first_few):
                missing_question_comments.append(fname)
                all_passed = False

    print("\n--- RESULTS ---")
    print(f"1. Program Files Exist: {len(REQUIRED_FILES) - len(missing_files)} / {len(REQUIRED_FILES)}")
    if missing_files:
        print(f"   [FAIL] Missing files: {missing_files}")
    else:
        print("   [PASS] All 50 program files are present in the folder.")

    print(f"2. File Integrity (Non-empty): {len(REQUIRED_FILES) - len(empty_files)} / {len(REQUIRED_FILES)}")
    if empty_files:
        print(f"   [FAIL] Empty files: {empty_files}")
    else:
        print("   [PASS] All 50 program files contain code.")

    print(f"3. Python Syntax Compilation: {len(REQUIRED_FILES) - len(syntax_errors)} / {len(REQUIRED_FILES)}")
    if syntax_errors:
        print(f"   [FAIL] Syntax errors:")
        for fn, err in syntax_errors:
            print(f"     - {fn}: {err}")
    else:
        print("   [PASS] All 50 program files compile cleanly with valid Python syntax.")

    print(f"4. Question Header Comments: {len(REQUIRED_FILES) - len(missing_question_comments)} / {len(REQUIRED_FILES)}")
    if missing_question_comments:
        print(f"   [FAIL] Files missing question comments: {missing_question_comments}")
    else:
        print("   [PASS] All 50 program files include the examination question as header comment.")

    datasets_dir = os.path.join(base_dir, "datasets")
    if os.path.exists(datasets_dir):
        csv_count = len(glob.glob(os.path.join(datasets_dir, "*.csv")))
        print(f"5. Datasets Directory: [PASS] Found {csv_count} CSV benchmark datasets.")
    else:
        print("5. Datasets Directory: [WARNING] datasets/ directory not found.")

    doc_files = ["question_index.md", "question_bank.md", "find_program.py", "requirements.txt"]
    for df in doc_files:
        p = os.path.join(base_dir, df)
        status = "[PASS]" if os.path.exists(p) else "[PENDING]"
        print(f"   Documentation/Utility: {df:20s} -> {status}")

    print("=" * 80)
    if all_passed:
        print("VERIFICATION COMPLETE: ALL CHECKS PASSED SUCCESSFULLY (100% READY)!")
    else:
        print("VERIFICATION FAILED: Please fix identified issues.")
    print("=" * 80)
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(verify_all())
