namespace Quantum.QSharpApplication1 {

	open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
	open Microsoft.Quantum.Measurement;
	open Microsoft.Quantum.Diagnostics;
	open Microsoft.Quantum.Arrays;
	open Microsoft.Quantum.Logical;
	open Microsoft.Quantum.Math

	operation EvolveUnderZ(
		strength: Double,
		time : Double,
		target : Qubit
	) : Unit is Adj + Ctl {
		Rz(2.0 * strength * time, target);
	}

	operation ApplyCNOT(register : Qubit[])
		: Unit is Adj + Ctl{
			CNOT(register[0], register[1]);
		}

	operation ApplyCNOT2(register: Qubit[])
		: Unit is Adj + Ctl{
			within{
				ApplyToEachCA(H, register);
			} apply {
				CNOT(register[1], register[0]);
			}
		}

	operation AssertCheck1() : Unit{
		AssertOperationsEqualReferenced(2, ApplyCNOT, ApplyCNOT2);
		Message("Woohoo!");
	}

	operation ApplyXUsingCNOTs(register: Qubit[])
		: Unit is Adj + Ctl
	{
		within{
			ApplyToEachCA(
				CNOT(register[0],_), Rest(register));
		}
		apply{
			X(register[0]);
		}
	}

	operation AssertCheck2() : Unit{
		AssertOperationsEqualReferenced(2, ApplyXUsingCNOTs, ApplyToEachCA(X,_));
		Message("Woohoo!");
	}

	operation ApplyRotationAboutXX(angle : Double, register: Qubit[])
		: Unit is Adj + Ctl{
		within{
			CNOT(register[0], register[1]);
		}
		apply{
			Rx(angle, register[0]);
		}
	}

	//Ising coupling gates
	operation AssertCheck3() : Unit{
		let angle = PI() / 3.0;
		AssertOperationsEqualReferenced(2, ApplyRotationAboutXX(angle, _),
			Exp([PauliX, PauliX], -angle/2.0,_));
		Message("Woohoo!");
	}
}