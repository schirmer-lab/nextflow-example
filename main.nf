#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

include { HOLY_WORKFLOW } from './workflows/holy_grail_workflow'

workflow  {
    HOLY_WORKFLOW()
}