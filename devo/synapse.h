#ifndef _SYNAPSE_H
#define _SYNAPSE_H

class SYNAPSE {

private:

	int sourceNeuronIndex;

	int targetNeuronIndex;

	double weight;

	double finalWeight;

	int transitionTime;
	
public:
        SYNAPSE(void);

	~SYNAPSE(void);

	int  Get_Source_Neuron_Index(void);

	int  Get_Target_Neuron_Index(void);

	double Get_Weight(int t);

	void Print(void);
};

#endif
