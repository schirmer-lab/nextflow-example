#!/usr/bin/env nextflow

nextflow.enable.dsl=2

include { PICK_RANDOM_LINE } from "../modules/scripts.nf"

workflow PICK_LINE_FROM_CLEANED_SCRIPT {
    take:
         holy_script
         file_prefix
         min_words

    main:
        line=PICK_RANDOM_LINE(holy_script,file_prefix,min_words)

    emit:
        line
}
