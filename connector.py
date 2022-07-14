class Connector:
	def case(self, file_path):
		app = win32.DispatchEx('HYSYS.Application.V12.0')
		case = app.SimulationCases.Open(file_path)
        case.Visible = 1
        
        return case