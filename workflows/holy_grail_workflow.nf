#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

include { DOWNLOAD_AND_CLEAN_SCRIPT } from '../subworkflows/get_script.nf'
include { PICK_LINE_FROM_CLEANED_SCRIPT as PICK_LINE } from '../subworkflows/pick_random_line.nf'

workflow holy_workflow {
    script_path = DOWNLOAD_AND_CLEAN_SCRIPT(params.holy_script_url, params.file_prefix)
    quote = PICK_LINE(script_path, params.quote_file_name, params.min_words)
    quote.view { it }
}
