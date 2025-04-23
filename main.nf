#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

include { holy_workflow } from './workflows/holy_grail_workflow'

workflow  {
    holy_workflow()
}