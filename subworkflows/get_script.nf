#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

include { DOWNLOAD_SCRIPT ; CLEAN_SCRIPT } from "../modules/scripts.nf"

workflow DOWNLOAD_AND_CLEAN_SCRIPT {
    take:
    holy_script_url
    holy_file_prefix

    main:
    downloaded = DOWNLOAD_SCRIPT(holy_script_url, holy_file_prefix)
    cleaned = CLEAN_SCRIPT(downloaded, holy_file_prefix)

    emit:
    cleaned
}
