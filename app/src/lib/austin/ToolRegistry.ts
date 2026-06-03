import { BOQService } from "@/services/austin/BOQService";
import { ValuationService } from "@/services/austin/ValuationService";
import { PropertyService } from "@/services/austin/PropertyService";
import { ContractorService } from "@/services/austin/ContractorService";
import { MortgageService } from "@/services/austin/MortgageService";
import { FraudService } from "@/services/austin/FraudService";

import { MortgageAffordabilityEngine } from "@/lib/austin/ranking/MortgageAffordabilityEngine";

export const ToolRegistry = {
  tools: {

    // 🧱 BOQ / Construction Intelligence
    boq: {
      async getMaterialPrices() {
        return BOQService.getMaterialPrices();
      },

      async getLaborRates() {
        return BOQService.getLaborRates();
      },

      async applyLocationMultiplier(data: any) {
        return BOQService.applyLocationMultiplier(data);
      },

      async calculateTotalCost(data: any) {
        return BOQService.calculateTotalCost(data);
      },

      async generateTable(data: any) {
        return BOQService.generateTable(data);
      }
    },

    // 🏠 Valuation Intelligence
    valuation: {
      async getPropertyData() {
        return ValuationService.getPropertyData();
      },

      async getComparables() {
        return ValuationService.getComparables();
      },

      async calculateMarketValue(data: any) {
        return ValuationService.calculateMarketValue(data);
      },

      async getRentalData() {
        return ValuationService.getRentalData();
      },

      async calculateROI(data: any) {
        return ValuationService.calculateROI(data);
      },

      async generateReport(data: any) {
        return ValuationService.generateReport(data);
      },

      async generateInvestmentScore(data: any) {
        return ValuationService.generateInvestmentScore(data);
      }
    },

    // 🧑‍🔧 Contractor Intelligence
    contractor: {
      async getProfile() {
        return ContractorService.getProfile();
      },

      async getHistory() {
        return ContractorService.getHistory();
      },

      async analyzeReviews() {
        return ContractorService.analyzeReviews();
      },

      async computeTrustScore(data: any) {
        return ContractorService.computeTrustScore(data);
      },

      async generateReport(data: any) {
        return ContractorService.generateReport(data);
      }
    },

    // 🏘 Property Intelligence
    property: {
      async search() {
        return PropertyService.search();
      },

      async rank(data: any) {
        return PropertyService.rank(data);
      },

      async formatListings(data: any) {
        return PropertyService.formatListings(data);
      }
    },

    // 💰 Mortgage Intelligence (NOW UPGRADED)
    mortgage: {
      async calculatePayment() {
        return MortgageService.calculatePayment();
      },

      async generateSchedule(data: any) {
        return MortgageService.generateSchedule(data);
      },

      // 🧠 NEW: AI affordability engine
      async calculateAffordability(data: any) {
        return MortgageAffordabilityEngine.calculate(data);
      }
    },

    // ⚠ Risk / Fraud Intelligence
    fraud: {
      async checkPatterns() {
        return FraudService.checkPatterns();
      },

      async scoreRisk(data: any) {
        return FraudService.scoreRisk(data);
      }
    }
  }
};