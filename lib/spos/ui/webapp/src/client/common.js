
import * as client from './spos'

var baseUrl = "http://127.0.0.1:8008";
export const ValuationClient = new client.ValuationClient(baseUrl);
export const ValuationDetailClient =  new client.ValuationDetailClient(baseUrl);
export const ValuationDetailTextClient =  new client.ValuationDetailTextClient(baseUrl);
export const SchoolClient = new client.SchoolClient(baseUrl);
export const SchoolClassClient = new client.SchoolClassClient(baseUrl);
export const PupilClient = new client.PupilClient(baseUrl);
export const PupilValuationSetClient = new client.PupilValuationSetClient(baseUrl);
export const PupilValuationClient = new client.PupilValuationClient(baseUrl);
export const ReportClient = new client.ReportClient(baseUrl);