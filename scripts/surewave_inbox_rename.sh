#!/bin/bash
# Rename, add preamble, and move surewave/background/new/*.md to surewave/background/
# Also copies the .xlsx and the two authoritative PDFs.
set -e
cd "$(dirname "$0")/../surewave/background/new" || exit 1
DEST=../

TODAY=2026-09-28

# mapping: original_stem|new_slug|doc_date|source_original_name
# (stem = filename without extension)
declare -A MAP
MAP["2023-12-08 - SUREWAVE Deliverable 3.3_final"]="2023-12-08_surewave_d3.3_final|2023-12-08|2023-12-08 - SUREWAVE Deliverable 3.3_final.docx"
MAP["D3.4 _Summary of global system design_final"]="2024-03-19_surewave_d3.4_summary_global_system_design|2024-03-19|D3.4 _Summary of global system design_final.docx"
MAP["D7.4_Economic_Assessment_final"]="2025-09-05_surewave_d7.4_economic_assessment|2025-09-05|D7.4_Economic_Assessment_final.docx"
MAP["D8.5_Dissemination,Exploitation&Communication_Master_Plan_Final"]="2024-04-29_surewave_d8.5_dissemination_exploitation_communication_master_plan|2024-04-29|D8.5_Dissemination,Exploitation&Communication_Master_Plan_Final.docx"
MAP["Grant Agreement-101083342-SUREWAVE"]="2022-09-20_surewave_grant_agreement_101083342|2022-09-20|Grant Agreement-101083342-SUREWAVE.pdf"
MAP["HE_SUREWAVE_Annex1-PartB_v2"]="2022-06-24_surewave_annex1_part_b_v2|2022-06-24|HE_SUREWAVE_Annex1-PartB_v2.docx"
MAP["HE_SUREWAVE_Proposal-SEP-210808360"]="2022-02-23_surewave_proposal_sep_210808360|2022-02-23|HE_SUREWAVE_Proposal-SEP-210808360.pdf"
MAP["SUREWAVE_CFD_Simulations_Plate"]="2023-03-10_surewave_cfd_simulations_plate|2023-03-10|SUREWAVE_CFD_Simulations_Plate.docx"
MAP["SUREWAVE_D1.5_Quality_Management_Plan"]="2024-04-05_surewave_d1.5_quality_management_plan|2024-04-05|SUREWAVE_D1.5_Quality_Management_Plan.docx"
MAP["SUREWAVE_D1.7_Data_Management_Plan_Release2_V1"]="2026-09-30_surewave_d1.7_data_management_plan_release2|2026-09-30|SUREWAVE_D1.7_Data_Management_Plan_Release2_V1.docx"
MAP["SUREWAVE_D1.8_IPR_Management_Plan_M36_V2"]="2026-09-30_surewave_d1.8_ipr_management_plan_m36|2026-09-30|SUREWAVE_D1.8_IPR_Management_Plan_M36_V2.docx"
MAP["SUREWAVE_D2.1_Use_case_scenario"]="2023-01-31_surewave_d2.1_use_case_scenario|2023-01-31|SUREWAVE_D2.1_Use_case_scenario.docx"
MAP["SUREWAVE_D2.2_Requirements_for_surface_mooring_system"]="2023-02-01_surewave_d2.2_requirements_surface_mooring_system|2023-02-01|SUREWAVE_D2.2_Requirements_for_surface_mooring_system.docx"
MAP["SUREWAVE_D2.3_general_loads_final"]="2023-01-31_surewave_d2.3_general_loads|2023-01-31|SUREWAVE_D2.3_general_loads_final.docx"
MAP["SUREWAVE_D2.4_stakeholder_advisory_board"]="2024-04-22_surewave_d2.4_stakeholder_advisory_board|2024-04-22|SUREWAVE_D2.4_stakeholder_advisory_board.docx"
MAP["SUREWAVE_D3.1_Design_description_of_internal_floating_PV_components"]="2023-06-26_surewave_d3.1_design_internal_floating_pv_components|2023-06-26|SUREWAVE_D3.1_Design_description_of_internal_floating_PV_components.docx"
MAP["SUREWAVE_D3.2_Floating_breakwater_design"]="2023-08-08_surewave_d3.2_floating_breakwater_design|2023-08-08|SUREWAVE_D3.2_Floating_breakwater_design.docx"
MAP["SUREWAVE_D4.1_Design and characterization of the new circular material solutions_v3.0"]="2024-01-18_surewave_d4.1_design_characterization_circular_materials|2024-01-18|SUREWAVE_D4.1_Design and characterization of the new circular material solutions_v3.0.docx"
MAP["SUREWAVE_D4.2_Development, validation and testing at laboratory level of the breakwater prototype_v1.0"]="2024-07-31_surewave_d4.2_lab_testing_breakwater_prototype|2024-07-31|SUREWAVE_D4.2_Development, validation and testing at laboratory level of the breakwater prototype_v1.0.docx"
MAP["SUREWAVE_D4.3_Breakwater prototype_v2.0"]="2024-08-30_surewave_d4.3_breakwater_prototype|2024-08-30|SUREWAVE_D4.3_Breakwater prototype_v2.0.docx"
MAP["SUREWAVE_D5.1.0_final"]="2024-04-16_surewave_d5.1|2024-04-16|SUREWAVE_D5.1.0_final.docx"
MAP["SUREWAVE_D5.3_Report on structural integrity assessment_v2.0_SD"]="2024-11-07_surewave_d5.3_structural_integrity_assessment|2024-11-07|SUREWAVE_D5.3_Report on structural integrity assessment_v2.0_SD.docx"
MAP["SUREWAVE_D5.4_Report on monitoring strategy_final"]="2024-09-30_surewave_d5.4_monitoring_strategy|2024-09-30|SUREWAVE_D5.4_Report on monitoring strategy_final.docx"
MAP["SUREWAVE_D5.5_Fatigue_crack_propagation_algorithms_R1"]="2025-04-30_surewave_d5.5_fatigue_crack_propagation_algorithms|2025-04-30|SUREWAVE_D5.5_Fatigue_crack_propagation_algorithms_R1.docx"
MAP["SUREWAVE_D5.6-SHMS_DEMO_R1"]="2025-06-13_surewave_d5.6_shms_demo|2025-06-13|SUREWAVE_D5.6-SHMS_DEMO_R1.docx"
MAP["SUREWAVE_D5.7-Modelling_Tools_Validation_Report_R01_Clean"]="2025-09-05_surewave_d5.7_modelling_tools_validation|2025-09-05|SUREWAVE_D5.7-Modelling_Tools_Validation_Report_R01_Clean.docx"
MAP["SUREWAVE_D6.1_Ultimate strength capacity"]="2024-09-12_surewave_d6.1_ultimate_strength_capacity|2024-09-12|SUREWAVE_D6.1_Ultimate strength capacity.docx"
MAP["SUREWAVE_D6.3"]="2025-02-12_surewave_d6.3|2025-02-12|SUREWAVE_D6.3.docx"
MAP["SUREWAVE_D7.3_Environmental_Report_V4"]="2025-10-06_surewave_d7.3_environmental_report|2025-10-06|SUREWAVE_D7.3_Environmental_Report_V4.docx"
MAP["SUREWAVE_D7.5_Social_Report_V3"]="2025-10-06_surewave_d7.5_social_report|2025-10-06|SUREWAVE_D7.5_Social_Report_V3.docx"
MAP["SUREWAVE_D7.6_Integrated_Sustainability_Report-v2"]="2025-11-05_surewave_d7.6_integrated_sustainability_report|2025-11-05|SUREWAVE_D7.6_Integrated_Sustainability_Report-v2.docx"
MAP["SUREWAVE_D8.2_Report on societal needs and engagement_V2"]="2025-09-30_surewave_d8.2_societal_needs_engagement|2025-09-30|SUREWAVE_D8.2_Report on societal needs and engagement_V2.docx"

for stem in "${!MAP[@]}"; do
  IFS='|' read -r slug ddate srcname <<< "${MAP[$stem]}"
  src_md="$stem.md"
  dst_md="$DEST$slug.md"
  if [ ! -f "$src_md" ]; then
    echo "MISSING: $src_md"
    continue
  fi
  # Write preamble to dst, then original content
  {
    printf '> Source: `%s` — Document date: %s — Converted: %s via pandoc/pdftotext\n\n---\n\n' "$srcname" "$ddate" "$TODAY"
    cat "$src_md"
  } > "$dst_md"
  echo "WROTE: $dst_md ($(wc -l < "$dst_md") lines)"
done
