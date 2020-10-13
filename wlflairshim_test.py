import wlflairshim

WOLFRAM_KERNEL_PATH = "/opt/Mathematica/SystemFiles/Kernel/Binaries/Linux-x86-64/WolframKernel"
tagger = wlflairshim.SequenceTagger(WOLFRAM_KERNEL_PATH)

print(tagger.predict("I went to Paris and bought some food from John Smith who works at Microsoft.", entity_types = ["City", "Financial"]))

tagger.close()