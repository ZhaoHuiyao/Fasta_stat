## cutadapt install

cutadapt官方手册：[Cutadapt — Cutadapt 4.0 documentation](https://cutadapt.readthedocs.io/en/stable/)

### miniconda install

基于miniconda进行安装，首先学会安装miniconda并简单使用（包括修改源、新建环境、激活环境等）

conda create -n cutadapt -c bioconda cutadapt

conda activate cutadapt

conda deactivate

### Basic use

Input file format; can be either 'fasta', 'fastq' or 'sra-fastq'，包括压缩文件，如：.gz/.bz2/.xz

共提供了3种adapt可能存在的位置：完整存在在一端、不完整存在在一端、完整存在在序列中间。分别使用三种不同参数识别3种情况。①若想把这三种都识别且去除，使用-a/-g ADAPTER；②若保留存在序列中间的情况，使用-a ADAPTERX/-g XADAPTER；③若只去除完整存在在一端的情况，使用-a ADAPTER$/-g ^ADAPTER

```shell
#去除3‘端序列—a SEQ
#去除5‘端序列—g SEQ
#--minimum-length reads最短长度
#设置核数-j N
#去除两端低质量reads：-q 15,10 -Q 15,15	表示去除第一个文件read5’端15以下和3‘端10以下的base；去除第一个文件read5’端15以下和3‘端15以下的base

#对于二代双端数据
cutadapt -a ADAPTER_FWD -A ADAPTER_REV -o out.1.fastq -p out.2.fastq reads.1.fastq reads.2.fastq

--minimum-length 10 --pair-filter=any  当其中一个出现长度小于10，则两个read都去除
--minimum-length 10 --pair-filter=both  只有两个read的长度小于10，这两个read才会去除

#cutadapt同样支持混测样的Demultiplexing
```



### Example 1

最简单的，单个文件去除adapt，adapt序列为：AGATCGGAAGAGCACACGTCTGAACTCCAGTCA

```shell
cutadapt -g AGATCGGAAGAGCACACGTCTGAACTCCAGTCA test.fa > test_clean.fa
```

