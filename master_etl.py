import subprocess

def run_step(script_name):
    print(f"\n🚀 Running: {script_name}")
    result = subprocess.run(["python", script_name])
    if result.returncode != 0:
        print(f"❌ {script_name} failed! Exiting.")
        exit(1)
    else:
        print(f"✅ {script_name} completed successfully.\n")

def main():
    print("========================================")
    print("📊 Electronic Stock Investment ETL Pipeline")
    print("========================================\n")

    run_step("generate_dummy_data.py")
    run_step("seed_investors.py")
    run_step("load_transactions.py")
    run_step("update_portfolio.py")
    run_step("analyze.py")

    print("🎉 ALL STEPS COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
