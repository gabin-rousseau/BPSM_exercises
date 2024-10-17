#!/usr/bin/bash

#cat Tcongo_genome/TriTrypDB-46_TcongolenseIL3000_2019_Genome.fasta | grep ">"
#cat Tcongo_genome/TriTrypDB-46_TcongolenseIL3000_2019_Genome.fasta | grep -c "chromosome"
#cat Tcongo_genome/TriTrypDB-46_TcongolenseIL3000_2019_Genome.fasta | grep -c "contig"

samplefile="${HOME}/Exercises/Pipeline/samples/Tco2.fqfiles"
index="${HOME}/Exercises/Pipeline/Tcongo_genome/Tcongo"
while IFS=$'\t' read line
do
        F_1=$(cut -f1 -s <<< "$line")
	if [[ "$F_1" == "Tco"* ]]; then
                sample1="${HOME}/Exercises/Pipeline/sequences/${F_1:0:3}-${F_1:3}_1.fq"
                sample2="${HOME}/Exercises/Pipeline/sequences/${F_1:0:3}-${F_1:3}_2.fq"
		outbt2="${HOME}/Exercises/Pipeline/alignments/${F_1}.log"
		outsmt="${HOME}/Exercises/Pipeline/alignments/${F_1}.bam"
		bowtie2 -x ${index} -1 ${sample1} -2 ${sample2} 2> ${outbt2} | \ #2> added to save alignment summaries
		samtools view -bhu | \
		samtools sort -o  ${outsmt}
	fi
done < ${samplefile}
