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

    cp "source/attendance_checker.py" "$root_dir/"
    cp "source/assets.csv" "$root_dir/Helpers/"
    cp "source/config.json" "$root_dir/Helpers/"
    cp "source/reports.log" "$root_dir/reports/"

    echo "Resource deployment completed."

    configure_thresholds
}