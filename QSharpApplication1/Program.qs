namespace Quantum.QSharpApplication1 {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
	open Microsoft.Quantum.Measurement;

    
    @EntryPoint()
    operation HelloQ () : Unit {
        Message("Hello quantum world!");
    }
	
    operation EstimateSuperposition () : (Int, Int) {
		mutable numZeros = 0;
		mutable numOnes = 0;
		use q = Qubit() {
			for idxTest in 1..100 {
				H(q);
				if (MResetZ(q) == Zero) {
					set numZeros += 1;
				} else {
					set numOnes += 1;
				}
			}
		}
		return (numZeros, numOnes);
	}
}