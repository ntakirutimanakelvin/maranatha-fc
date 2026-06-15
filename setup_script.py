#!/bin/bash

setup_project() {
    echo "=== Deploy agent NTAKIRUTIMANA Kelvin ==="

    read -p "Enter project identifier: " project_id

    root_dir="attendance_tracker_${project_id}"

    echo "Generating project workspace..."

    mkdir -p "$root_dir"
    mkdir -p "$root_dir/Helpers"
    mkdir -p "$root_dir/reports"

    echo "Workspace prepared successfully."

    echo "Copying required application resources..."

    cp "resources/attendance_checker.py" "$root_dir/"
    cp "resources/assets.csv" "$root_dir/Helpers/"
    cp "resources/config.json" "$root_dir/Helpers/"
    cp "resources/reports.log" "$root_dir/reports/"

    echo "Resource deployment completed."

    configure_thresholds
}

configure_thresholds() {
    echo ""
    echo "=== Threshold Stage ==="

    read -p "Would you like to customize attendance limits? (y/n): " choice

    case "$choice" in
        y|Y)

            while true
            do
                read -p "Enter warning percentage: " warn_limit

                if [[ "$warn_limit" =~ ^[0-9]+$ ]]; then
                    break
                fi

                echo "Invalid value. Numbers only."
            done

            while true
            do
                read -p "Enter failure percentage: " fail_limit

                if [[ "$fail_limit" =~ ^[0-9]+$ ]]; then
                    break
                fi

                echo "Invalid value. Numbers only."
            done

            sed -Ei \
                -e 's|("warning": )[0-9]+|\1'"$warn_limit"'|' \
                -e 's|("failure": )[0-9]+|\1'"$fail_limit"'|' \
                "$root_dir/resources/config.json"

            echo "Thresholds updated successfully."
            ;;
        *)
            echo "Using default attendance limits."
            ;;
    esac

    run_diagnostics
}

run_diagnostics() {
    echo ""
    echo "=== Environment Verification ==="

    printf "Checking Python installation... "

    if command -v python3 >/dev/null 2>&1
    then
        echo "Python is AVAILABLE"
        python3 --version
    else
        echo "Python is NOT DETECTED"
    fi

    echo ""
    echo "Verifying workspace contents..."

    check_path "$root_dir" "Workspace Directory"
    check_path "$root_dir/attendance_checker.py" "Main Python Script"
    check_path "$root_dir/resources/assets.csv" "Asset Data File"
    check_path "$root_dir/resources/config.json" "Configuration File"
    check_path "$root_dir/logs/reports.log" "Report Log"
}

check_path() {
    local target="$1"
    local description="$2"

    if [ -e "$target" ]
    then
        echo "Present: $description"
    else
        echo "MISSING: $description"
    fi
}