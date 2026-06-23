export class BOQService {

  // 📊 BOQ table generator
  static async generateTable(data: any) {
    const breakdown = data?.breakdown || [];

    return {
      items: breakdown,
      total: breakdown.reduce((sum: number, item: any) => sum + (item.cost || 0), 0)
    };
  }

}


