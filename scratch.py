import re
import pandas as pd

input_file_1 = """
	

		"""


def extract_data_and_create_pivot(data):
    test_pattern = re.compile(
        r"Vdd \(mV\): (\d+).*?Frequency \(MHz\): (\d+).*?"
        r"RxDQLeft Rank0 Width = (-?\d+pS).*?"
        r"RxDQRight Rank0 Width = (-?\d+pS).*?"
        r"TxDQLeft Rank0 Width = (-?\d+pS).*?"
        r"TxDQRight Rank0 Width = (-?\d+pS).*?"
        r"RxVrefLow Rank0 Width = (-?\d+mV).*?"
        r"RxVrefHigh Rank0 Width = (-?\d+mV).*?"
        r"TxVrefLow Rank0 Width = (-?\d+mV).*?"
        r"TxVrefHigh Rank0 Width = (-?\d+mV).*?"
        r"CmdLeft Rank0 Width = (-?\d+pS).*?"
        r"CmdRight Rank0 Width = (-?\d+pS).*?"
        r"RxDQLeft Rank1 Width = (-?\d+pS).*?"
        r"RxDQRight Rank1 Width = (-?\d+pS).*?"
        r"TxDQLeft Rank1 Width = (-?\d+pS).*?"
        r"TxDQRight Rank1 Width = (-?\d+pS).*?"
        r"RxVrefLow Rank1 Width = (-?\d+mV).*?"
        r"RxVrefHigh Rank1 Width = (-?\d+mV).*?"
        r"TxVrefLow Rank1 Width = (-?\d+mV).*?"
        r"TxVrefHigh Rank1 Width = (-?\d+mV).*?"
        r"CmdLeft Rank1 Width = (-?\d+pS).*?"
        r"CmdRight Rank1 Width = (-?\d+pS)",
        re.DOTALL
    )

    extracted_data = []
    for match in test_pattern.finditer(data):
        voltage = int(match.group(1))
        frequency = int(match.group(2))

        data_dict = {
            "Voltage": voltage,
            "Frequency": frequency,
            "RxDQLeft Rank0 Width": match.group(3),
            "RxDQRight Rank0 Width": match.group(4),
            "TxDQLeft Rank0 Width": match.group(5),
            "TxDQRight Rank0 Width": match.group(6),
            "RxVrefLow Rank0 Width": match.group(7),
            "RxVrefHigh Rank0 Width": match.group(8),
            "TxVrefLow Rank0 Width": match.group(9),
            "TxVrefHigh Rank0 Width": match.group(10),
            "CmdLeft Rank0 Width": match.group(11),
            "CmdRight Rank0 Width": match.group(12),
            "RxDQLeft Rank1 Width": match.group(13),
            "RxDQRight Rank1 Width": match.group(14),
            "TxDQLeft Rank1 Width": match.group(15),
            "TxDQRight Rank1 Width": match.group(16),
            "RxVrefLow Rank1 Width": match.group(17),
            "RxVrefHigh Rank1 Width": match.group(18),
            "TxVrefLow Rank1 Width": match.group(19),
            "TxVrefHigh Rank1 Width": match.group(20),
            "CmdLeft Rank1 Width": match.group(21),
            "CmdRight Rank1 Width": match.group(22)
        }
        extracted_data.append(data_dict)

    df = pd.DataFrame(extracted_data)

    pivot_table = df.set_index(["Voltage", "Frequency"])

    return pivot_table


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

pivot_table = extract_data_and_create_pivot(input_file_1)
pivot_table.to_html("output.html")
